
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os
import requests


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
# PERSONA PROMPTS
# ==============================

PERSONA_PROMPTS = {

    "Technical Expert": """
You are a senior technical support engineer.

Provide:
- Detailed technical explanation
- Root cause analysis
- Troubleshooting steps
- Technical recommendations

Use professional technical language.

Only use the provided context.
""",

   
"Frustrated User": """
You are an empathetic AI customer support specialist.

Rules:
- Start with empathy
- Reassure the user
- Use calm and simple language
- Give numbered troubleshooting steps
- Avoid technical jargon
- End with supportive guidance

Keep responses conversational and helpful.

Only use the provided context.
""",


    "Business Executive": """
You are an executive support advisor.

Focus on:
- Business impact
- Resolution timeline
- Operational stability
- Clear concise communication

Keep the response short and professional.

Only use the provided context.
"""
}


# ==============================
# FORMAT RAG CONTEXT
# ==============================

def format_context(context):

    formatted = ""

    for item in context:

        formatted += f"\nSOURCE: {item['source']}\n"

        formatted += item["text"]

        formatted += "\n\n"

    return formatted


# ==============================
# GENERATE RESPONSE
# ==============================





def generate_response(query, persona, context):

    system_prompt = PERSONA_PROMPTS.get(
        persona,
        PERSONA_PROMPTS["Business Executive"]
    )

    formatted_context = format_context(context)

    final_prompt = f"""
{system_prompt}

CONTEXT:
{formatted_context}

USER QUESTION:
{query}

Generate a clear, accurate, persona-adapted customer support response using ONLY the provided context.

If the context does not contain the answer, say:
"I could not find enough information in the knowledge base."
"""

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]



# ==============================
# TESTING
# ==============================

if __name__ == "__main__":

    sample_context = [
        {
            "source": "password_reset.md",
            "text": "Click forgot password and reset using email."
        }
    ]

    response = generate_response(
        query="I cannot login to my account",
        persona="Frustrated User",
        context=sample_context
    )

    print(response)

