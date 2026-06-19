
from src.classifier import classify_persona
from src.rag_pipeline import retrieve_context
from src.generator import generate_response
from src.escalator import should_escalate


# ==============================
# MAIN APPLICATION LOOP
# ==============================

def main():

    print("\n===================================")
    print(" AI Persona-Adaptive Support Agent ")
    print("===================================\n")

    while True:

        query = input("User Query: ")

        if query.lower() == "exit":
            print("Exiting application...")
            break

        # --------------------------
        # Persona Classification
        # --------------------------

        persona = classify_persona(query)

        print(f"\nDetected Persona: {persona}")

        # --------------------------
        # Retrieve RAG Context
        # --------------------------

        context = retrieve_context(query)

        # --------------------------
        # Confidence Score
        # --------------------------

        score = 0.85

        # --------------------------
        # Escalation Check
        # --------------------------

        escalation = should_escalate(
            query,
            score
        )

        if escalation:

            print("\n⚠️ Escalation Recommended")
            print("Reason: Sensitive issue or low confidence\n")

        # --------------------------
        # Generate Response
        # --------------------------

        response = generate_response(
            query=query,
            persona=persona,
            context=context
        )

        # --------------------------
        # Final Output
        # --------------------------

        print("\nAI Response:\n")

        print(response)

        print("\n-----------------------------------\n")


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":

    main()

