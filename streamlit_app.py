
import streamlit as st
from src.classifier import classify_persona
from src.rag_pipeline import retrieve_context
from src.generator import generate_response
from src.escalator import should_escalate


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Persona AI Support Agent",
    page_icon="🤖",
    layout="wide"
)


# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stTextArea textarea {
    font-size: 16px;
}

.response-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #333;
    margin-top: 10px;
}

.metric-card {
    background-color: #161B22;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    border: 1px solid #30363D;
}

.persona-tag {
    padding: 8px 16px;
    border-radius: 20px;
    display: inline-block;
    font-weight: bold;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🤖 AI Support Agent")
    st.caption(
    "Adaptive AI customer support powered by RAG, persona detection, and escalation intelligence."
)

    st.markdown("---")

    st.info(
        "Try different queries to observe persona adaptation, RAG retrieval, and escalation behavior."
    )

    st.title("🧪 Explore with these Sample Test Queries")

    st.markdown("---")

    st.markdown("### 😡 Frustrated User")

    st.code(
        "Your login system is terrible and not working"
    )

    st.markdown("### 👨‍💻 Technical Expert")

    st.code(
        "API authentication returning 401 unauthorized error"
    )

    st.markdown("### 💼 Business Executive")

    st.code(
        "Need clarification regarding enterprise billing policy"
    )

    st.markdown("---")

    st.markdown("### 🔐 Security Issue")

    st.code(
        "I think my account was hacked"
    )

    st.markdown("### 💳 Payment Failure")

    st.code(
        "My payment failed but amount was deducted"
    )

  

    st.markdown("---")


    st.info(
        "This AI system adapts responses based on customer persona and retrieves context-aware answers from the knowledge base."
    )


# =====================================
# HERO SECTION
# =====================================

st.markdown("""
<h1 style='text-align:center;'>
🤖 Persona-Adaptive AI Support Agent
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; font-size:18px; color:gray;'>
AI-powered customer support with Retrieval-Augmented Generation and adaptive communication styles.
</p>
""", unsafe_allow_html=True)

st.divider()


# =====================================
# QUERY INPUT
# =====================================

query = st.text_area(
    "Customer Query",
    placeholder="Example: API authentication returning 401 unauthorized error...",
    height=150
)


# =====================================
# GENERATE BUTTON
# =====================================

if st.button("🚀 Generate AI Response", use_container_width=True):

    if not query.strip():

        st.warning("Please enter a customer query.")

    else:

        # =====================================
        # PERSONA DETECTION
        # =====================================

        persona = classify_persona(query)

        # =====================================
        # RAG RETRIEVAL
        # =====================================

        context = retrieve_context(query)

        # =====================================
        # ESCALATION CHECK
        # =====================================

        score = 0.85

        escalation = should_escalate(
            query,
            score
        )

        # =====================================
        # TOP METRICS
        # =====================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Detected Persona",
                persona
            )

        with col2:
            st.metric(
                "Retrieved Chunks",
                len(context)
            )

        with col3:
            st.metric(
                "Escalation",
                "YES" if escalation else "NO"
            )

        st.divider()

        # =====================================
        # ESCALATION ALERT
        # =====================================

        if escalation:

            st.error(
                "⚠️ Human escalation recommended due to sensitive or high-risk issue."
            )

        else:

            st.success(
                "✅ No escalation required."
            )

        # =====================================
        # GENERATE RESPONSE
        # =====================================

        with st.spinner("Generating intelligent response..."):

            response = generate_response(
                query=query,
                persona=persona,
                context=context
            )

        # =====================================
        # RESPONSE SECTION
        # =====================================

        st.subheader("💬 AI Response")

        st.markdown(
            f"""
            <div class="response-box">
            {response}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # =====================================
        # KNOWLEDGE SOURCES
        # =====================================

        st.subheader("📚 Retrieved Knowledge Sources")

        for item in context:

            with st.expander(f"📄 {item['source']}"):

                st.write(item["text"])

