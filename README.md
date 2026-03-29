<div align="center">

# 🩺 DoctorAI-QA v2

### *AI-Powered Multilingual Healthcare Assistant*

**Ask health questions in any language. Get answers in yours.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/🚀_Live_App-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://doctorai-app-v2-nysyz8d239s7dxnvkyjzfm.streamlit.app/)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-FFD21E?style=for-the-badge)](https://huggingface.co/syedazah777/DoctorAI-QA)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)](LICENSE)
[![Languages](https://img.shields.io/badge/Languages-5-orange?style=for-the-badge)](#-supported-languages)

<br/>

> ⚠️ **For educational purposes only. Not a substitute for professional medical advice.**

<br/>

![DoctorAI-QA Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-f07040?style=for-the-badge) https://doctorai-app-v2-nysyz8d239s7dxnvkyjzfm.streamlit.app/

</div>

---

## 📖 Table of Contents

- [What is DoctorAI-QA?](#-what-is-doctoraiqa)
- [Key Features](#-key-features)
- [Supported Languages](#-supported-languages)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Stage 1 → Stage 2](#-stage-1--stage-2-improvements)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Built for Octoverse Hackathon](#-built-for-octoverse-hackathon)

---

## 🌍 What is DoctorAI-QA?

**DoctorAI-QA** is an open-source AI healthcare assistant fine-tuned on medical datasets using **LoRA + Unsloth** on a GPT-OSS 20B base model.

Millions of people search for health information online — but most resources are in English only. DoctorAI-QA bridges this gap by:

- 🗣️ **Understanding 5 languages** — including romanized text like `naku jwaram undi` or `mujhe bukhar hai`
- 🔊 **Speaking back** in the user's native language via text-to-speech
- 🩺 **Guiding users** through a structured symptom assessment
- 🚨 **Flagging urgency** — High, Medium, or Low — for every query
- 🔒 **Staying responsible** — every response includes safety disclaimers

---

## 🚀 Key Features

| Feature | Description |
|--------|-------------|
| 🌐 **Auto Language Detection** | Detects language from native script AND romanized Roman text |
| 💬 **Multilingual Chat** | Full answers in English, Hindi, Telugu, Marathi, Arabic |
| 🔊 **Voice Output (TTS)** | Reads answers aloud in the detected language using gTTS |
| 🎤 **Voice Input** | Speak your question — converted to text automatically |
| 🩺 **Symptom Checker** | 3-step guided flow → urgency assessment → send to chat |
| 🚨 **Severity Detection** | Auto-flags 🔴 High / 🟡 Medium / 🟢 Low urgency |
| 📊 **Analytics Dashboard** | Confidence scores, trend graph, consultation history |
| ℹ️ **About Page** | Full project info, tech stack, and model details |
| 🎨 **Premium UI** | Animated dark theme with glassmorphism chat bubbles |

---

## 🗣️ Supported Languages

| Flag | Language | Native Script | Romanized Input |
|------|----------|--------------|-----------------|
| 🇬🇧 | **English** | ✅ | ✅ |
| 🇮🇳 | **Hindi** | ✅ देवनागरी | ✅ `mujhe bukhar hai` |
| 🇮🇳 | **Telugu** | ✅ తెలుగు | ✅ `naku jwaram undi` |
| 🇮🇳 | **Marathi** | ✅ मराठी | ✅ `mla taap aahe` |
| 🇸🇦 | **Arabic** | ✅ عربي | ✅ `ladaya hmaa wa suda` |

> **No language selection needed.** Just type naturally — DoctorAI detects and responds automatically.

---

## 🏗️ Tech Stack

```
┌─────────────────────────────────────────────────────┐
│                    DoctorAI-QA v2                   │
├─────────────────┬───────────────────────────────────┤
│  Base Model     │  GPT-OSS 20B (OpenAI)             │
│  Quantization   │  4-bit (memory efficient)         │
│  Fine-tuning    │  LoRA via Unsloth + HuggingFace   │
│  Training       │  Google Colab (GPU)               │
├─────────────────┼───────────────────────────────────┤
│  Interface      │  Streamlit + Custom CSS           │
│  Inference API  │  OpenRouter (LLaMA 3 8B)          │
│  TTS            │  gTTS (hi, te, mr, ar, en)        │
│  Voice Input    │  SpeechRecognition                │
├─────────────────┼───────────────────────────────────┤
│  Model Hosting  │  HuggingFace Spaces               │
│  App Hosting    │  Streamlit Cloud                  │
│  License        │  Apache 2.0                       │
└─────────────────┴───────────────────────────────────┘
```

---

## 📁 Project Structure

```
DoctorAI-QA-v2/
│
├── 📄 app.py                    ← Main chat interface (Home)
│
├── 📁 pages/
│   ├── 📄 about.py              ← Project info, tech stack, model details
│   ├── 📄 dashboard.py          ← Analytics: confidence scores, history graph
│   └── 📄 symptom_checker.py    ← 3-step guided symptom assessment
│
├── 📄 .env                      ← API keys (not committed to git)
├── 📄 .gitignore
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ⚡ Getting Started

### Prerequisites
- Python 3.10+
- OpenRouter API key (free at [openrouter.ai](https://openrouter.ai))

### 1. Clone the repo
```bash
git clone https://github.com/alizahh-7/DoctorAI-QA-v2.git
cd DoctorAI-QA-v2
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment
Create a `.env` file:
```env
OPENROUTER_API_KEY=your_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Open in browser
```
http://localhost:8501
```

---

## 💬 Example Queries

Try these in the chat:

```
🇬🇧  What are the early signs of diabetes?
🇮🇳  Mujhe bukhar aur sar dard hai
🇮🇳  Naku jwaram undi, em cheyali?
🇮🇳  Mla taap aahe aani dokyat dukhtay
🇸🇦  ladaya hmaa wa suda
🇮🇳  Bhai mera pet bahut dard kar raha hai
🇬🇧  How to lower blood pressure naturally?
```

---

## 📈 Stage 1 → Stage 2 Improvements

| Feature | Stage 1 | Stage 2 |
|---------|:-------:|:-------:|
| Interface | Gradio / Colab | Full Streamlit App |
| Languages | 🇬🇧 English only | 🌍 5 Languages |
| Language Detection | ❌ | ✅ Script + Romanized |
| Voice Output (TTS) | ❌ | ✅ Native language audio |
| Voice Input | ❌ | ✅ Speech recognition |
| Symptom Checker | ❌ | ✅ 3-step guided flow |
| Severity Detection | ❌ | ✅ 🔴🟡🟢 Auto-flag |
| Analytics Dashboard | ❌ | ✅ Confidence + history |
| About Page | ❌ | ✅ Full project info |
| UI Design | Plain Gradio | ✨ Animated dark theme |
| Safety Disclaimers | Basic | ✅ Contextual per response |

---

## 🧠 How It Works

```
User types query (any language / any script)
        ↓
Language Detection Engine
├── Unicode script scan (देवनागरी / عربي / తెలుగు)
└── Romanized keyword matching (hinglish / romanized telugu / arabic)
        ↓
Language-specific system prompt injected
        ↓
LLaMA 3 8B via OpenRouter API
(fine-tuned DoctorAI-QA persona)
        ↓
Structured response:
├── Brief explanation
├── Key points (bullets)
├── When to see a doctor
└── Confidence score
        ↓
Severity detection (keyword scan)
        ↓
Auto TTS → Audio plays in native language
        ↓
Response + Safety disclaimer shown
        ↓
Dashboard updated (confidence, history)
```

---

## 🏆 Built for Octoverse Hackathon 2026

This project was built as a **Stage 2 submission** for the Octoverse Hackathon — refining and expanding upon the Stage 1 MVP with multilingual support, voice features, and a complete UI overhaul.

**Judging criteria alignment:**

| Criteria | How we address it |
|----------|------------------|
| 🎨 Creativity & Uniqueness | Romanized multilingual detection — first of its kind |
| ⚙️ Functionality | 5 features: chat, TTS, symptom checker, dashboard, voice input |
| 🖥️ Design & Aesthetics | Animated glassmorphism dark UI with custom sidebar nav |
| 💡 Innovation | Healthcare AI accessible to non-English speakers globally |

---

## 👩‍💻 Author

**Syeda Alizah**

[![HuggingFace](https://img.shields.io/badge/🤗_Model-syedazah777/DoctorAI--QA-FFD21E?style=flat-square)](https://huggingface.co/syedazah777/DoctorAI-QA)
[![GitHub](https://img.shields.io/badge/GitHub-alizahh--7-181717?style=flat-square&logo=github)](https://github.com/alizahh-7)

---

## 📄 License

```
Apache License 2.0
Copyright 2026 Syeda Alizah

Licensed under the Apache License, Version 2.0
```

---

<div align="center">

**Made with ❤️ for the world's multilingual majority**

*If this helped you, give it a ⭐ on GitHub!*

</div>
