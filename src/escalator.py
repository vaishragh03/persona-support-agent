
def should_escalate(query, score):

    sensitive_words = [
        "billing",
        "refund",
        "legal",
        "account hacked",
        "security breach",
        "payment failed",
        "unauthorized"
    ]

    negative_words = [
        "angry",
        "frustrated",
        "worst",
        "terrible",
        "not working",
        "disappointed"
    ]

    query_lower = query.lower()

    # Low confidence retrieval
    if score < 0.45:
        return True

    # Sensitive business/security issues
    if any(word in query_lower for word in sensitive_words):
        return True

    # Strong negative sentiment
    if any(word in query_lower for word in negative_words):
        return True

    return False

