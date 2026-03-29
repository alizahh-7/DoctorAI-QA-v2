import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Insights 📊", page_icon="📊")

st.title("📊 AI Response Insights Dashboard")

# DEFAULT VALUES
confidence = st.session_state.get("confidence", 90)
reasoning = st.session_state.get(
    "reasoning",
    "• AI analyzes symptoms\n• Matches with medical patterns\n• Suggests safe response"
)
source = st.session_state.get("source", "General Medical Knowledge")
disclaimer = st.session_state.get(
    "disclaimer",
    "This is not a professional medical diagnosis."
)

# METRIC
st.metric("🧠 Confidence Score", f"{confidence}%")
st.progress(confidence / 100)

# DETAILS
st.markdown("### 🧠 How AI Thought")
st.markdown(reasoning)

st.markdown("### 📚 Knowledge Source")
st.info(source)

st.markdown("### ⚠️ Medical Disclaimer")
st.warning(disclaimer)

# STATUS
if confidence > 90:
    st.success("✅ High confidence response")
elif confidence > 75:
    st.info("ℹ️ Moderate confidence")
else:
    st.error("⚠️ Low confidence - consult doctor")

# =========================
# 📈 GRAPH SECTION
# =========================
st.markdown("## 📈 Confidence Trend")

if "history" in st.session_state and len(st.session_state.history) > 0:
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df["confidence"])
else:
    st.info("No data for graph yet.")

# =========================
# 📜 HISTORY SECTION
# =========================
st.markdown("## 📜 Previous Consultations")

if "history" in st.session_state and len(st.session_state.history) > 0:

    for item in reversed(st.session_state.history[-5:]):
        st.markdown(f"""
**🧑 Question:** {item['question']}  
**🤖 Answer:** {item['answer']}  
**🧠 Confidence:** {item['confidence']}%  
---
""")
else:
    st.info("No past consultations yet.")

# FOOTER
st.caption("Built with ❤️ for Hackathon Demo")