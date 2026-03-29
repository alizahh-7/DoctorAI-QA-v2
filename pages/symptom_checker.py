import streamlit as st

st.set_page_config(page_title="Symptom Checker", page_icon="🩺", layout="wide")

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
.block-container { max-width: 700px; margin: auto; padding-top: 2rem; }

h1 {
    background: linear-gradient(90deg, #60a5fa, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2rem !important;
    font-weight: 600 !important;
}
p, li { color: #c8d8f0; }

/* Step card */
.step-card {
    background: rgba(15,30,60,0.8);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 20px;
}
.step-label {
    font-size: 12px;
    color: #3b82f6;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.step-question {
    font-size: 18px;
    font-weight: 600;
    color: #e2eeff;
    margin-bottom: 20px;
}

/* Progress bar */
.prog-wrap {
    background: rgba(59,130,246,0.1);
    border-radius: 4px;
    height: 6px;
    margin-bottom: 24px;
    overflow: hidden;
}
.prog-fill {
    height: 100%;
    background: linear-gradient(90deg, #3b82f6, #60a5fa);
    border-radius: 4px;
    transition: width 0.4s ease;
}

/* Option buttons */
.stButton > button {
    background: rgba(59,130,246,0.08) !important;
    color: #93c5fd !important;
    border: 1px solid rgba(59,130,246,0.25) !important;
    border-radius: 10px !important;
    font-size: 14px !important;
    padding: 12px 16px !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 6px !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: rgba(59,130,246,0.2) !important;
    border-color: #3b82f6 !important;
    color: #bfdbfe !important;
    transform: translateX(4px) !important;
}

/* Result card */
.result-high {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.35);
    border-left: 4px solid #ef4444;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 16px;
}
.result-medium {
    background: rgba(245,158,11,0.08);
    border: 1px solid rgba(245,158,11,0.35);
    border-left: 4px solid #f59e0b;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 16px;
}
.result-low {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.3);
    border-left: 4px solid #22c55e;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 16px;
}
.result-title { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
.result-body  { font-size: 13px; color: #94a3b8; line-height: 1.7; }

.summary-box {
    background: rgba(15,30,60,0.7);
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 16px;
}
.summary-row { display: flex; justify-content: space-between; padding: 5px 0; border-bottom: 1px solid rgba(59,130,246,0.08); font-size: 13px; }
.summary-key { color: #64748b; }
.summary-val { color: #93c5fd; font-weight: 500; }

.action-btn {
    background: linear-gradient(135deg, #1d4ed8, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 12px 20px !important;
    width: 100% !important;
    margin-bottom: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──
if "sym_step" not in st.session_state: st.session_state.sym_step = 0
if "sym_data" not in st.session_state: st.session_state.sym_data = {}

# ── HEADER ──
st.markdown("# 🩺 Symptom Checker")
st.markdown('<p style="color:#64748b;font-size:14px;">Answer 3 quick questions to assess your symptoms</p>', unsafe_allow_html=True)

# ── STEPS DATA ──
STEPS = [
    {
        "label": "Step 1 of 3 · Category",
        "question": "What are you experiencing?",
        "field": "category",
        "opts": [
            "😣 Pain or Discomfort",
            "🌡️ Fever or Infection Signs",
            "🫃 Digestive Issues",
            "❤️ Heart or Breathing Issues",
            "🧠 Mental Health Concerns",
            "🌿 Skin or Allergy Issues",
            "💊 Medication Side Effects",
            "🦴 Muscle or Joint Issues",
        ]
    },
    {
        "label": "Step 2 of 3 · Duration",
        "question": "How long have you had this?",
        "field": "duration",
        "opts": [
            "⚡ Less than 24 hours",
            "📅 1 to 3 days",
            "📆 4 to 7 days",
            "🗓️ Over a week",
            "🔁 Chronic / Recurring (months)",
        ]
    },
    {
        "label": "Step 3 of 3 · Severity",
        "question": "How severe is it right now?",
        "field": "severity",
        "opts": [
            "🟢 Mild — I can manage it",
            "🟡 Moderate — It's affecting my daily life",
            "🔴 Severe — Very uncomfortable or painful",
            "🚨 Emergency — I need help immediately",
        ]
    }
]

step = st.session_state.sym_step

# ── PROGRESS BAR ──
progress = min(step / 3, 1.0)
st.markdown(f"""
<div class="prog-wrap">
  <div class="prog-fill" style="width:{int(progress*100)}%"></div>
</div>
""", unsafe_allow_html=True)

# ── SHOW STEP ──
if step < 3:
    current = STEPS[step]
    st.markdown(f"""
<div class="step-card">
  <div class="step-label">{current['label']}</div>
  <div class="step-question">{current['question']}</div>
</div>
""", unsafe_allow_html=True)

    for opt in current["opts"]:
        if st.button(opt, key=f"opt_{step}_{opt}"):
            st.session_state.sym_data[current["field"]] = opt
            st.session_state.sym_step += 1
            st.rerun()

    if step > 0:
        if st.button("← Back", key="back_btn"):
            st.session_state.sym_step -= 1
            last_field = STEPS[step - 1]["field"]
            st.session_state.sym_data.pop(last_field, None)
            st.rerun()

# ── RESULT ──
else:
    data     = st.session_state.sym_data
    category = data.get("category", "")
    duration = data.get("duration", "")
    severity = data.get("severity", "")

    st.markdown("### ✅ Assessment Complete")

    # Summary box
    st.markdown(f"""
<div class="summary-box">
  <div class="summary-row"><span class="summary-key">Symptom</span><span class="summary-val">{category}</span></div>
  <div class="summary-row"><span class="summary-key">Duration</span><span class="summary-val">{duration}</span></div>
  <div class="summary-row"><span class="summary-key">Severity</span><span class="summary-val">{severity}</span></div>
</div>
""", unsafe_allow_html=True)

    # Result based on severity
    if "🚨" in severity:
        st.markdown("""
<div class="result-high">
  <div class="result-title" style="color:#fca5a5;">🚨 Emergency — Seek Immediate Help</div>
  <div class="result-body">
    Your symptoms suggest an emergency situation. Please call emergency services (112 / 911)
    or go to the nearest hospital immediately. Do not wait.
  </div>
</div>""", unsafe_allow_html=True)

    elif "🔴" in severity or ("🟡" in severity and "Over a week" in duration):
        st.markdown("""
<div class="result-high">
  <div class="result-title" style="color:#fca5a5;">🔴 High Concern — See a Doctor Soon</div>
  <div class="result-body">
    Your symptoms are serious or have persisted for a long time.
    Please schedule a doctor's appointment as soon as possible — within 24 hours if possible.
    Do not self-medicate.
  </div>
</div>""", unsafe_allow_html=True)

    elif "🟡" in severity or "4 to 7 days" in duration or "Over a week" in duration:
        st.markdown("""
<div class="result-medium">
  <div class="result-title" style="color:#fcd34d;">🟡 Moderate — Monitor Carefully</div>
  <div class="result-body">
    Your symptoms are moderate. Monitor them closely over the next 24–48 hours.
    If they worsen or don't improve, consult a doctor. Stay hydrated and rest well.
  </div>
</div>""", unsafe_allow_html=True)

    else:
        st.markdown("""
<div class="result-low">
  <div class="result-title" style="color:#86efac;">🟢 Low Concern — General Care</div>
  <div class="result-body">
    Your symptoms appear mild and recent. Rest, stay hydrated, and monitor.
    Most mild symptoms resolve on their own in 1–3 days.
    See a doctor if symptoms worsen or persist beyond a week.
  </div>
</div>""", unsafe_allow_html=True)

    # Ask DoctorAI button
    st.markdown("**Want a detailed explanation?**")
    ask_q = f"I have {category} for {duration}. Severity is {severity}. What could this be and what should I do?"

    if st.button("💬 Ask DoctorAI for Details", key="ask_ai"):
        st.session_state["pending"] = ask_q
        st.switch_page("app.py")

    st.markdown('<p style="font-size:12px;color:#334155;margin-top:4px;">This will take you to the chat with your symptoms pre-filled.</p>', unsafe_allow_html=True)

    # Reset
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↺ Check Another Symptom", key="reset_btn"):
        st.session_state.sym_step = 0
        st.session_state.sym_data = {}
        st.rerun()

    # Disclaimer
    st.markdown("""
<div style="background:rgba(245,158,11,0.07);border:1px solid rgba(245,158,11,0.25);
border-radius:8px;padding:12px 16px;margin-top:16px;font-size:12px;color:#92400e;color:#fcd34d;">
⚠️ This is a basic symptom assessment tool for educational use only.
It is NOT a medical diagnosis. Always consult a licensed doctor for professional advice.
</div>
""", unsafe_allow_html=True)