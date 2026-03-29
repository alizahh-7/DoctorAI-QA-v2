import streamlit as st

st.set_page_config(page_title="About DoctorAI-QA", page_icon="ℹ️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #050d1a 0%, #0a1628 50%, #0d1f3c 100%);
    min-height: 100vh;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071020 0%, #0c1a35 100%);
    border-right: 1px solid rgba(59,130,246,0.2);
}
.block-container { max-width: 860px; margin: auto; padding-top: 2rem; }

h1 {
    background: linear-gradient(90deg, #60a5fa, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2rem !important;
    font-weight: 600 !important;
}
h2, h3 { color: #93c5fd !important; }
p, li { color: #c8d8f0; line-height: 1.8; }

.card {
    background: rgba(15,30,60,0.7);
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 18px;
}
.card-title {
    font-size: 15px;
    font-weight: 600;
    color: #60a5fa;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.card p, .card li { font-size: 13px; color: #94a3b8; }

.badge {
    display: inline-block;
    background: rgba(59,130,246,0.15);
    border: 1px solid rgba(59,130,246,0.3);
    color: #93c5fd;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 12px;
    margin: 3px;
}
.tag {
    display: inline-block;
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.25);
    color: #86efac;
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 12px;
    margin: 3px;
}
.warning-box {
    background: rgba(245,158,11,0.08);
    border: 1px solid rgba(245,158,11,0.3);
    border-left: 3px solid #f59e0b;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 13px;
    color: #fcd34d;
    margin-top: 10px;
}
.stat-box {
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 10px;
    padding: 16px;
    text-align: center;
}
.stat-num { font-size: 28px; font-weight: 700; color: #60a5fa; }
.stat-label { font-size: 12px; color: #64748b; margin-top: 2px; }
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.markdown("# ℹ️ About DoctorAI-QA")
st.markdown('<p style="color:#64748b;font-size:14px;">Open-source AI Healthcare Assistant · Built for Octoverse Hackathon</p>', unsafe_allow_html=True)

st.markdown("---")

# ── STATS ROW ──
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-box"><div class="stat-num">20B</div><div class="stat-label">Model Parameters</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><div class="stat-num">5</div><div class="stat-label">Languages Supported</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><div class="stat-num">LoRA</div><div class="stat-label">Fine-tuning Method</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-box"><div class="stat-num">v2.0</div><div class="stat-label">Current Version</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── WHAT IS IT ──
st.markdown("""
<div class="card">
  <div class="card-title">🧠 What is DoctorAI-QA?</div>
  <p>
    DoctorAI-QA is an open-source AI model fine-tuned on healthcare datasets for educational question-answering.
    It provides clear, reasoning-based answers about diseases, symptoms, medications, and lifestyle — in multiple languages.
  </p>
  <p style="margin-top:8px;">
    Built to bridge the gap between complex medical information and everyday understanding,
    DoctorAI-QA makes reliable health knowledge accessible to students, educators, and the general public worldwide.
  </p>
</div>
""", unsafe_allow_html=True)

# ── TWO COLUMNS ──
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
<div class="card">
  <div class="card-title">⚙️ Technical Stack</div>
  <ul>
    <li><b>Base Model:</b> GPT-OSS 20B</li>
    <li><b>Fine-tuning:</b> LoRA adapters via Unsloth</li>
    <li><b>Quantization:</b> 4-bit (memory efficient)</li>
    <li><b>Training:</b> Google Colab (GPU)</li>
    <li><b>Interface:</b> Streamlit</li>
    <li><b>TTS:</b> Google Text-to-Speech (gTTS)</li>
    <li><b>Hosting:</b> HuggingFace + Streamlit Cloud</li>
    <li><b>License:</b> Apache-2.0 (fully open-source)</li>
  </ul>
</div>
""", unsafe_allow_html=True)

with col_right:
    st.markdown("""
<div class="card">
  <div class="card-title">🌍 Supported Languages</div>
  <ul>
    <li>🇬🇧 <b>English</b> — Full support</li>
    <li>🇮🇳 <b>Hindi</b> — देवनागरी + Hinglish</li>
    <li>🇮🇳 <b>Telugu</b> — తెలుగు + Romanized</li>
    <li>🇮🇳 <b>Marathi</b> — मराठी + Romanized</li>
    <li>🇸🇦 <b>Arabic</b> — عربي + Romanized</li>
  </ul>
  <p style="margin-top:8px;">Auto-detects language from your input — no manual selection needed!</p>
</div>
""", unsafe_allow_html=True)

# ── FEATURES ──
st.markdown("""
<div class="card">
  <div class="card-title">🚀 Key Features</div>
""", unsafe_allow_html=True)

features = [
    ("💬", "Multilingual Chat", "Auto-detects and responds in 5 languages including Hindi, Telugu, Marathi, Arabic"),
    ("🩺", "Symptom Checker", "3-step guided flow to assess symptoms and urgency level"),
    ("🔊", "Voice / Read Aloud", "Text-to-speech support in native language for accessibility"),
    ("📊", "Response Dashboard", "Confidence scores, reasoning steps, and consultation history"),
    ("🚨", "Severity Detection", "Automatically flags high / medium / low urgency health questions"),
    ("🔒", "Safety First", "Every response includes medical disclaimers and doctor referral guidance"),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
<div style="background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.15);
border-radius:10px;padding:14px;margin-bottom:12px;">
  <div style="font-size:22px;margin-bottom:6px;">{icon}</div>
  <div style="font-size:13px;font-weight:600;color:#60a5fa;margin-bottom:4px;">{title}</div>
  <div style="font-size:12px;color:#64748b;line-height:1.5;">{desc}</div>
</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── HOW IT WAS BUILT ──
st.markdown("""
<div class="card">
  <div class="card-title">🏗️ How It Was Built</div>
  <p><b>Stage 1</b> — Fine-tuned GPT-OSS 20B on healthcare Q&A datasets using LoRA + Unsloth in Google Colab.
  Deployed a working Gradio demo on HuggingFace Spaces.</p>
  <p style="margin-top:8px;"><b>Stage 2 (v2.0)</b> — Rebuilt the interface with Streamlit, added multilingual support
  for 5 languages, symptom checker, voice output, severity detection, and a response analytics dashboard.</p>
</div>
""", unsafe_allow_html=True)

# ── TAGS ──
st.markdown("**Built with:**")
tags = ["Python", "Streamlit", "LoRA", "Unsloth", "GPT-OSS", "HuggingFace",
        "gTTS", "OpenRouter", "LLaMA", "Healthcare AI", "Open Source"]
st.markdown(" ".join(f'<span class="tag">{t}</span>' for t in tags), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── DISCLAIMER ──
st.markdown("""
<div class="warning-box">
⚠️ <b>Medical Disclaimer:</b> DoctorAI-QA is intended for educational and informational purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare provider for medical decisions.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#334155;font-size:12px;">DoctorAI-QA v2 · Built for Octoverse Hackathon · Apache-2.0 License</p>', unsafe_allow_html=True)