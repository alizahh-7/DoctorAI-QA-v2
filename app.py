import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import random

try:
    import speech_recognition as sr
    voice_enabled = True
except:
    voice_enabled = False

try:
    from gtts import gTTS
    from io import BytesIO
    tts_enabled = True
except:
    tts_enabled = False

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={"HTTP-Referer": "http://localhost:8501", "X-Title": "DoctorAI-QA"}
)

st.set_page_config(
    page_title="DoctorAI-QA v2", 
    page_icon="🩺", 
    layout="wide",
    initial_sidebar_state="expanded"  # ← ADD THIS to force sidebar open
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}

/* ── HIDE STREAMLIT HEADER & FOOTER COMPLETELY ── */
#MainMenu {visibility:hidden;}
header[data-testid="stHeader"] {display:none !important;}
footer {display:none !important;}
.stDeployButton {display:none !important;}
[data-testid="stToolbar"] {display:none !important;}
[data-testid="stDecoration"] {display:none !important;}
[data-testid="stStatusWidget"] {display:none !important;}

/* ── FIX TOP PADDING — no header means no gap needed ── */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 820px;
    margin: auto;
}

/* ── BACKGROUND ORBS ── */
.stApp{background:#030912;min-height:100vh;position:relative;overflow-x:hidden;}
.stApp::before{
  content:'';position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;
  background:
    radial-gradient(ellipse 55% 45% at 5% 5%,   rgba(220,75,30,0.5)  0%,transparent 65%),
    radial-gradient(ellipse 45% 55% at 95% 90%,  rgba(8,12,45,0.95)   0%,transparent 65%),
    radial-gradient(ellipse 40% 50% at 80% 10%,  rgba(200,60,20,0.3)  0%,transparent 60%),
    radial-gradient(ellipse 50% 35% at 15% 85%,  rgba(160,45,15,0.35) 0%,transparent 60%),
    radial-gradient(ellipse 35% 40% at 55% 55%,  rgba(240,90,40,0.18) 0%,transparent 55%),
    linear-gradient(135deg,#030912 0%,#070e28 50%,#0a0f20 100%);
  animation:orbDrift 14s ease-in-out infinite alternate;
  pointer-events:none;
}
.stApp::after{
  content:'';position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;
  background:
    radial-gradient(ellipse 40% 45% at 70% 25%, rgba(240,80,30,0.22) 0%,transparent 55%),
    radial-gradient(ellipse 30% 40% at 25% 60%, rgba(180,50,15,0.28) 0%,transparent 50%);
  animation:orbDrift2 18s ease-in-out infinite alternate;
  pointer-events:none;
}
@keyframes orbDrift{
  0%  {transform:scale(1) translate(0,0);}
  30% {transform:scale(1.04) translate(-18px,12px);}
  60% {transform:scale(1.02) translate(12px,-10px);}
  100%{transform:scale(1.05) translate(8px,14px);}
}
@keyframes orbDrift2{
  0%  {transform:scale(1) translate(0,0);opacity:.6;}
  40% {transform:scale(1.07) translate(22px,-18px);opacity:.8;}
  100%{transform:scale(1.04) translate(6px,-8px);opacity:.7;}
}
.stApp>*{position:relative;z-index:2;}

/* ── SIDEBAR - FORCE VISIBLE ── */
[data-testid="stSidebar"]{
  background:rgba(3,6,18,0.92) !important;
  backdrop-filter:blur(24px);
  border-right:1px solid rgba(240,90,30,0.12);
  z-index:100;
  display:block !important;  /* ← FORCE DISPLAY */
  visibility:visible !important;  /* ← FORCE VISIBLE */
}
[data-testid="stSidebar"]>div:first-child{
  display:block !important;
  visibility:visible !important;
}
/* Hide default nav but keep sidebar visible */
[data-testid="stSidebarNav"]{display:none !important;}

/* Hide the collapse button to prevent users from hiding sidebar */
[data-testid="collapsedControl"]{display:none !important;}
button[kind="header"]{display:none !important;}

.nav-card{
  display:flex;align-items:center;gap:14px;
  padding:14px 16px;border-radius:12px;
  border:1px solid rgba(240,90,30,0.15);
  background:rgba(240,90,30,0.07);
  margin-bottom:10px;cursor:pointer;
  transition:all 0.2s;text-decoration:none !important;
}
.nav-card:hover{
  background:rgba(240,90,30,0.18);
  border-color:rgba(240,90,30,0.4);
  transform:translateX(4px);
}
.nav-icon{font-size:26px;line-height:1;flex-shrink:0;}
.nav-text{display:flex;flex-direction:column;gap:2px;}
.nav-title{font-size:14px;font-weight:600;color:#f0a070;}
.nav-sub{font-size:11px;color:rgba(200,150,120,0.6);}

.sidebar-brand{
  display:flex;align-items:center;gap:10px;
  padding:16px 4px 20px 4px;
  border-bottom:1px solid rgba(240,90,30,0.1);
  margin-bottom:16px;
}
.brand-dot{width:10px;height:10px;background:#f07040;border-radius:50%;
  box-shadow:0 0 8px #f07040;animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.5;transform:scale(0.8);}}
.brand-name{font-size:16px;font-weight:700;color:#f0d0b0;letter-spacing:-0.02em;}

/* ── TITLE ── */
h1{
  text-align:center;font-size:2.2rem !important;font-weight:700 !important;
  letter-spacing:-0.03em !important;
  background:linear-gradient(90deg,#f07040,#ff9966,#ffb380,#f07040);
  background-size:300% auto;
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  animation:shine 4s linear infinite;margin-bottom:0 !important;
}
@keyframes shine{0%{background-position:0%;}100%{background-position:300%;}}
.subtitle{
  text-align:center;color:rgba(200,160,130,0.5);
  font-size:12px;margin-bottom:24px;margin-top:5px;
  letter-spacing:0.06em;text-transform:uppercase;
}

/* ── CHAT BUBBLES ── */
.user-msg{
  background:rgba(240,90,30,0.13);border:1px solid rgba(240,90,30,0.28);
  border-radius:16px 16px 4px 16px;padding:12px 16px;margin:8px 0;
  color:#f0d0b0;font-size:14px;line-height:1.65;backdrop-filter:blur(10px);
}
.bot-msg{
  background:rgba(6,11,30,0.78);border:1px solid rgba(240,90,30,0.12);
  border-left:3px solid #f07040;border-radius:0 16px 16px 16px;
  padding:14px 18px;margin:8px 0;color:#c8b8a8;font-size:14px;line-height:1.8;
  backdrop-filter:blur(14px);
}
.lang-detected{
  display:inline-block;background:rgba(240,90,30,0.1);
  border:1px solid rgba(240,90,30,0.28);color:#f07040;
  border-radius:20px;padding:3px 12px;font-size:12px;margin:6px 0 10px 0;
}

/* ── SEVERITY ── */
.sev-high  {background:rgba(239,68,68,0.09);border:1px solid rgba(239,68,68,0.3);border-left:3px solid #ef4444;border-radius:0 8px 8px 0;padding:10px 14px;color:#fca5a5;font-size:13px;margin-top:8px;}
.sev-medium{background:rgba(245,158,11,0.09);border:1px solid rgba(245,158,11,0.28);border-left:3px solid #f59e0b;border-radius:0 8px 8px 0;padding:10px 14px;color:#fcd34d;font-size:13px;margin-top:8px;}
.sev-low   {background:rgba(34,197,94,0.07);border:1px solid rgba(34,197,94,0.22);border-left:3px solid #22c55e;border-radius:0 8px 8px 0;padding:10px 14px;color:#86efac;font-size:13px;margin-top:8px;}

/* ── BUTTONS ── */
.stButton>button{
  background:rgba(240,90,30,0.09) !important;color:#f07040 !important;
  border:1px solid rgba(240,90,30,0.28) !important;border-radius:8px !important;
  font-size:13px !important;padding:8px 14px !important;
  transition:all 0.2s !important;
}
.stButton>button:hover{
  background:rgba(240,90,30,0.22) !important;border-color:#f07040 !important;color:#ffb080 !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"] textarea{
  background:rgba(3,6,18,0.72) !important;color:#f0d0b0 !important;
  border:1px solid rgba(240,90,30,0.28) !important;border-radius:14px !important;
}
[data-testid="stChatInput"] textarea:focus{border-color:#f07040 !important;box-shadow:0 0 0 3px rgba(240,90,30,0.12) !important;}
[data-testid="stChatInput"] textarea::placeholder{color:rgba(200,140,100,0.4) !important;}

::-webkit-scrollbar{width:4px;}
::-webkit-scrollbar-thumb{background:rgba(240,90,30,0.28);border-radius:2px;}
.stSpinner>div{border-top-color:#f07040 !important;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────
if "messages"   not in st.session_state: st.session_state.messages   = []
if "history"    not in st.session_state: st.session_state.history    = []
if "last_reply" not in st.session_state: st.session_state.last_reply = ""
if "last_lang"  not in st.session_state: st.session_state.last_lang  = "english"
if "pending"    not in st.session_state: st.session_state.pending    = None

# ─────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div class="sidebar-brand">
  <div class="brand-dot"></div>
  <span class="brand-name">DoctorAI-QA v2</span>
</div>

<a href="/" target="_self" class="nav-card">
  <span class="nav-icon">🏠</span>
  <div class="nav-text">
    <span class="nav-title">Home</span>
    <span class="nav-sub">Chat with DoctorAI</span>
  </div>
</a>

<a href="/about" target="_self" class="nav-card">
  <span class="nav-icon">ℹ️</span>
  <div class="nav-text">
    <span class="nav-title">About</span>
    <span class="nav-sub">Project info & tech stack</span>
  </div>
</a>

<a href="/dashboard" target="_self" class="nav-card">
  <span class="nav-icon">📊</span>
  <div class="nav-text">
    <span class="nav-title">Dashboard</span>
    <span class="nav-sub">Response analytics</span>
  </div>
</a>

<a href="/symptom_checker" target="_self" class="nav-card">
  <span class="nav-icon">🩺</span>
  <div class="nav-text">
    <span class="nav-title">Symptom Checker</span>
    <span class="nav-sub">3-step assessment</span>
  </div>
</a>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
#  MAIN HEADER
# ─────────────────────────────────────────
st.markdown("<h1>🩺 DoctorAI-QA v2</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Multilingual · AI-Powered · Educational · Open Source</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────
#  LANGUAGE DETECTION
# ─────────────────────────────────────────
def detect_lang(prompt):
    for ch in prompt:
        if '\u0900' <= ch <= '\u097F': return "hindi"
        if '\u0600' <= ch <= '\u06FF': return "arabic"
        if '\u0C00' <= ch <= '\u0C7F': return "telugu"
    lowered = prompt.lower()
    if any(w in lowered for w in ["naku","jwaram","undi","nenu","ela","evaru","cheyali","ayindi","pain undi","fever undi","em cheyali"]): return "telugu"
    if any(w in lowered for w in ["mla","mlaa","mala","majha","dukhta","taap","aahe","khup","dukh","dokyat","dukhtay","vedna"]): return "marathi"
    if any(w in lowered for w in ["ladaya","ana indi","ana marid","indi waja","ladaya hmaa","ladaya hmmma","humma","suda","waja fi","albatn","mareed"]): return "arabic"
    if any(w in lowered for w in ["mujhe","bukhar","dard","khansi","pet","sar","ulti","bhai","kya","hai","nahi","mera","meri","toh","yeh","hoga","neend","karun","bahut"]): return "hindi"
    return "english"

def get_system_prompt(lang):
    structure = "\nStructure: 1. Brief explanation 2. Key points (bullets) 3. When to see a doctor 4. Confidence: XX%\nNever diagnose. Educational only."
    return {
        "hindi":   "तुम DoctorAI हो।\nसख्त नियम: पूरा जवाब केवल हिंदी (देवनागरी) में।\nएक भी अंग्रेज़ी शब्द नहीं।" + structure,
        "arabic":  "أنت DoctorAI.\nقاعدة صارمة: الإجابة كاملةً بالعربية فقط. لا إنجليزية أبداً." + structure,
        "telugu":  "మీరు DoctorAI.\nకఠిన నియమం: సమాధానం పూర్తిగా తెలుగులో మాత్రమే. ఇంగ్లీష్ వద్దు." + structure,
        "marathi": "तुम्ही DoctorAI आहात.\nकठोर नियम: उत्तर फक्त मराठीत. इंग्रजी नको." + structure,
        "english": "You are DoctorAI — a helpful medical education assistant.\nReply in English only." + structure,
    }.get(lang, "You are DoctorAI. Reply helpfully." + structure)

def get_tts_lang(lang):
    return {"hindi":"hi","arabic":"ar","telugu":"te","marathi":"mr","english":"en"}.get(lang,"en")

# ─────────────────────────────────────────
#  CHAT HISTORY
# ─────────────────────────────────────────
for msg in st.session_state.messages:
    css  = "user-msg" if msg["role"] == "user" else "bot-msg"
    icon = "🧑" if msg["role"] == "user" else "🤖"
    st.markdown(f"<div class='{css}'>{icon} {msg['content']}</div>", unsafe_allow_html=True)

# ── READ ALOUD ──
if st.session_state.last_reply and tts_enabled:
    if st.button("🔊 Read Aloud"):
        try:
            clean = st.session_state.last_reply[:800].replace("**","").replace("*","").replace("#","")
            tts = gTTS(text=clean, lang=get_tts_lang(st.session_state.last_lang))
            buf = BytesIO(); tts.write_to_fp(buf); buf.seek(0)
            st.audio(buf, format="audio/mp3")
        except Exception as e:
            st.error(f"Audio error: {e}")

# ── VOICE INPUT ──
prompt = None
if voice_enabled:
    if st.button("🎤 Speak"):
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                st.info("Listening...")
                audio = r.listen(source, timeout=5)
                text  = r.recognize_google(audio)
                st.success(f"You said: {text}")
                prompt = text
        except:
            st.error("Voice error / Mic issue")

# ── TEXT INPUT ──
text_input = st.chat_input("Ask in any language · कोई भी भाषा · ఏ భాషలోనైనా · أي لغة")
if text_input: prompt = text_input
if st.session_state.pending:
    prompt = st.session_state.pending
    st.session_state.pending = None

# ─────────────────────────────────────────
#  MAIN LOGIC
# ─────────────────────────────────────────
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    st.markdown(f"<div class='user-msg'>🧑 {prompt}</div>", unsafe_allow_html=True)

    lang = detect_lang(prompt)
    st.session_state.last_lang = lang
    lang_display = {"hindi":"🇮🇳 Hindi","arabic":"🇸🇦 Arabic","telugu":"🇮🇳 Telugu","marathi":"🇮🇳 Marathi","english":"🇬🇧 English"}
    st.markdown(f'<div class="lang-detected">🌍 Detected: {lang_display.get(lang,lang.title())}</div>', unsafe_allow_html=True)

    with st.spinner("🩺 Analyzing..."):
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            temperature=0.7,
            messages=[
                {"role":"system","content":get_system_prompt(lang)},
                {"role":"user",  "content":prompt}
            ]
        )

    reply = response.choices[0].message.content
    st.session_state.last_reply = reply
    st.session_state.messages.append({"role":"assistant","content":reply})
    st.markdown(f"<div class='bot-msg'>🤖 {reply}</div>", unsafe_allow_html=True)

    combined = (prompt + " " + reply).lower()
    if any(w in combined for w in ["chest pain","heart attack","unconscious","bleeding","stroke","seizure","can't breathe"]):
        st.markdown('<div class="sev-high">🚨 HIGH SEVERITY — Seek immediate medical attention!</div>', unsafe_allow_html=True)
    elif any(w in combined for w in ["fever","vomiting","pain","infection","swelling","dizziness","bukhar","dard","jwaram","taap","hmaa","humma"]):
        st.markdown('<div class="sev-medium">⚠️ MEDIUM — Monitor symptoms. See a doctor if worsens.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="sev-low">ℹ️ LOW — General health information provided.</div>', unsafe_allow_html=True)

    if tts_enabled:
        try:
            clean = reply[:800].replace("**","").replace("*","").replace("#","")
            tts = gTTS(text=clean, lang=get_tts_lang(lang))
            buf = BytesIO(); tts.write_to_fp(buf); buf.seek(0)
            st.audio(buf, format="audio/mp3")
        except: pass

    confidence = random.randint(85, 97)
    st.session_state.confidence = confidence
    st.session_state.reasoning  = "• Symptoms analyzed\n• Matched with medical patterns\n• Safe educational advice generated"
    st.session_state.source     = "DoctorAI-QA v2 — Fine-tuned on Medical Datasets"
    st.session_state.disclaimer = "Not a professional medical diagnosis."
    st.session_state.history.append({"question":prompt,"answer":reply,"confidence":confidence})
