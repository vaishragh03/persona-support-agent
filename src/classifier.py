
def classify_persona(query):

    query = query.lower()

    # Technical users
    technical_keywords = [
        "api",
        "database",
        "server",
        "authentication",
        "integration",
        "error",
        "bug",
        "endpoint"
    ]

    # Business users
    business_keywords = [
        "revenue",
        "billing",
        "subscription",
        "invoice",
        "cost",
        "executive",
        "business"
    ]

    # Frustrated users
    frustrated_keywords = [
        "angry",
        "frustrated",
        "worst",
        "terrible",
        "not working",
        "issue",
        "problem"
    ]

    if any(word in query for word in technical_keywords):
        return "Technical Expert"

    elif any(word in query for word in frustrated_keywords):
        return "Frustrated User"

    elif any(word in query for word in business_keywords):
        return "Business Executive"

    return "Business Executive"

