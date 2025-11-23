# 🧠 AI System Architect Specification

**Project:** Streamlit-Based PDF Study Assistant (Gemini OpenAgents SDK)  
**Version:** Ultra-Clean Zero-Bloat Architecture  

---

## 1. System Objective

Design a **minimal, fast, production-clean intelligent study companion** that:

### Core Tasks
- Extract text from academic PDFs
- Produce structured study notes and concept summaries
- Generate MCQ/mixed-format quizzes
- Run fully in Streamlit with a smooth, distraction-free UI
- Use **Google Gemini (`gemini-2.0-flash`)** through OpenAgents SDK (not OpenAI SDK)

### Restrictions
- No TensorFlow
- No heavy PDF libraries
- No extra dependencies

### Allowed Libraries
- `streamlit`
- `PyPDF2`
- `openai-agents`
- `python-dotenv`

---

## 2. Architectural Summary

### A. Core Engine

**Powered by a single intelligent agent: StudyAgent**  

- **Model:** `gemini-2.0-flash`  
- **Wrapped using:** OpenAgents SDK  
- **Tools bound:**  
  - `extract_pdf_text` (PyPDF2)  
  - `summarize_text` (Agent)  
  - `generate_quiz` (Agent)  

#### Agent System Prompt
> “You are a Pedagogical AI System.  
> First summarize the input text into clear study notes.  
> Then generate an assessment-quality quiz based strictly on the text.”

---

### B. Application Components

#### 1. `tools.py`
Contains the lowest-level utility functions:

| Function | Responsibility |
|----------|----------------|
| `extract_pdf_text(path)` | Read PDF → plain text |
| `clean_text(text)` | Remove extra spaces, artifacts |
| `format_quiz_output(raw)` | Convert agent JSON → readable quiz |

#### 2. `agent.py`
Defines the Gemini agent:

**Responsibilities:**
- Initialize OpenAgents Agent
- Register all tool functions
- Provide `run_summary(text)` and `run_quiz(text)` wrappers
- Ensure consistent request format to Gemini

#### 3. `app.py`
Provides backend functions for Streamlit:

**Responsibilities:**
- Handle uploaded PDF
- Call tools & agent methods
- Preprocess and store session state
- Deliver clean outputs to UI

#### 4. `main.py`
Streamlit UI layer:

**Responsibilities:**
- PDF uploader
- Summary viewer
- Quiz generator button
- Light/Dark toggle
- Responsive layout + scrollable sections

---

## 3. Folder Structure

task4/
│── .gemini/
│ └── settings.json
│── gemini.md
│── main.py
│── pyproject.toml
│── README.md
│── .env
└── uv.lock





## 4. Detailed Functional Architecture

### tools.py — Utility Layer
**Responsibilities:**
- Extremely small and fast
- Follow Zero-Bloat rule
- Only handle raw operations (PDF → text, formatting)

**Contents:**
- Extract PDF text
- Clean text
- Format quiz from agent output

### agent.py — AI Reasoning Layer
**Responsibilities:**
- Create and configure the Gemini agent
- Bind tools according to OpenAgents SDK syntax
- Provide two public methods:
  - `agent_summary(text)`
  - `agent_quiz(text)`

**Behavior:**
- Always summarize first
- Then generate quiz
- Use the same text extracted from PDF

### app.py — Business Logic Layer
**Responsibilities:**
- Glue between UI and agent
- Load PDF and extract text
- Request summary and quiz
- Cache results in Streamlit session_state

**Outputs:**
- Clean summary
- Clean quiz
- Stable error-free execution

### main.py — Streamlit Interface Layer
**Responsibilities:**
- Full user experience
- File upload widget
- Summary container
- Quiz container
- Modern UI (cards, subtle shadows, dark mode)
- Calls methods from `app.py`

**Sections:**
- Header
- Upload Area
- Summary Card
- Quiz Card

---

## 5. Flow Diagram

[User Uploads PDF]
|
v
tools.extract_pdf_text()
|
v
agent.agent_summary()
|
v
agent.agent_quiz()
|
v
Streamlit UI displays summary + quiz


## 6. Example End-to-End User Flow

1. User uploads `"Chapter 3 – Neuroanatomy.pdf"`
2. Text extraction using PyPDF2
3. Agent receives text → produces summary:
   - Key points
   - Definitions
   - Concepts
4. Quiz generated (MCQs mixed with reasoning questions)
5. UI displays:
   - Scrollable summary card
   - Quiz card with answers hidden

---

## 7. Testing Scenarios

| Test | Expected Result |
|------|----------------|
| Small PDF | Summary + quiz instantly |
| Large PDF (50 pages) | Summary concise, quiz accurate |
| Complex formatting | Cleaned text output |
| Repeated uploads | Session state resets cleanly |
| Missing PDF | Graceful stop |

---

## 8. Unique Improvements Over the Original Version

- ✅ Fully architected like an enterprise AI system
- ✅ Four-layer structure (tools → agent → app → UI)
- ✅ Standardized agent prompts and workflows
- ✅ Modular design for future scaling (memory, RAG, etc.)
- ✅ Professional system-level documentation
- ✅ Zero-bloat enforced at architectural level
- ✅ Clean abstraction boundaries
- ✅ Ready-to-implement code files

---

## 9. Next Steps / Options

You can now generate:

- **Option A:** Full working code for all files (`main.py)
- **Option B:** `pyproject.toml` + `README.md`
- **Option C:** Entire zip folder structure with code
- **Option D:** Same architecture but with streaming responses

