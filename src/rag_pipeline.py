
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import chromadb


# ==============================
# LOAD ENV VARIABLES
# ==============================

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


# ==============================
# GEMINI CLIENT
# ==============================

gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==============================
# CHROMA DB SETUP
# ==============================

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="support_kb"
)


# ==============================
# LOAD DOCUMENTS
# ==============================


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FOLDER = BASE_DIR / "data"


def load_documents(data_folder=DATA_FOLDER):

    documents = []

    for file in os.listdir(data_folder):

        path = data_folder / file

        # Markdown / Text
        if file.endswith(".md") or file.endswith(".txt"):

            with open(path, "r", encoding="utf-8") as f:

                documents.append({
                    "source": file,
                    "content": f.read()
                })

        # PDF
        elif file.endswith(".pdf"):

            reader = PdfReader(path)

            pdf_text = ""

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    pdf_text += extracted + "\n"

            documents.append({
                "source": file,
                "content": pdf_text
            })

    return documents



# ==============================
# CHUNK DOCUMENTS
# ==============================

def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=40
    )

    chunks = []

    for doc in documents:

        split_chunks = splitter.split_text(
            doc["content"]
        )

        for chunk in split_chunks:

            chunks.append({
                "text": chunk,
                "source": doc["source"]
            })

    return chunks


# ==============================
# GENERATE EMBEDDINGS
# ==============================


def get_embedding(text):

    response = gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values




# ==============================
# CREATE VECTOR DATABASE
# ==============================

def create_vector_db(chunks):
    try: collection.delete(where={}) 
    except: pass
    for idx, chunk in enumerate(chunks):

        embedding = get_embedding(
            chunk["text"]
        )

        collection.add(
            ids=[str(idx)],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[
                {
                    "source": chunk["source"]
                }
            ]
        )

        print(f"Stored chunk {idx}")


# ==============================
# RETRIEVE DOCUMENTS
# ==============================

def retrieve(query, top_k=3):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


# ==============================
# CLEAN CONTEXT OUTPUT
# ==============================

def retrieve_context(query):

    results = retrieve(query)

    context = []

    docs = results["documents"][0]
    meta = results["metadatas"][0]

    for d, m in zip(docs, meta):

        context.append({
            "text": d,
            "source": m["source"]
        })

    return context


# ==============================
# TESTING
# ==============================

if __name__ == "__main__":

    print("Loading documents...")

    docs = load_documents()

    print(f"Loaded {len(docs)} documents")

    print("Chunking documents...")

    chunks = chunk_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("Creating vector database...")

    create_vector_db(chunks)

    print("Testing retrieval...")

    query = "How do I reset my password?"

    context = retrieve_context(query)

    print("\nRetrieved Context:\n")

    for item in context:

        print("SOURCE:", item["source"])
        print(item["text"])
        print("-" * 50)

