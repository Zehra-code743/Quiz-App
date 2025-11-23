🧠 AI System Architect Specification
Project: Streamlit-Based PDF Study Assistant (Gemini OpenAgents SDK)
Version: Ultra-Clean Zero-Bloat Architecture
1. System Objective
Design a minimal, fast, production-clean intelligent study companion that:

Core Tasks:

Extract text from academic PDFs

Produce structured study notes and concept summaries

Generate MCQ/mixed-format quizzes

Run fully in Streamlit with a smooth, distraction-free UI

Use Google Gemini (gemini-2.0-flash) through OpenAgents SDK — not OpenAI SDK

Restrictions:

No TensorFlow

No heavy PDF libraries

No extra dependencies

Allowed Libraries:

streamlit

PyPDF2

openai-agents

python-dotenv

Architectural Summary:

Core Engine:
The system is powered by a single intelligent agent embedded within main.py. The agent uses the gemini-2.0-flash model wrapped via OpenAgents SDK. Internally, it handles PDF text extraction, text cleaning, summary generation, and quiz generation.

Agent System Prompt:
“You are a Pedagogical AI System. First summarize the input text into clear study notes. Then generate an assessment-quality quiz based strictly on the text.”

Application Component: main.py

Responsibilities:

PDF upload interface

Text extraction and cleaning

Summary generation using the Gemini agent

Quiz generation using the Gemini agent

Display outputs in Streamlit UI

Optional Light/Dark mode toggle

Scrollable summary and quiz containers

Key Features:

Minimal zero-bloat design

Async processing for agent calls

Single-file modular structure

Ready-to-implement, production-ready code

Clean abstraction, easy to extend for future features (memory, retrieval-augmented generation, streaming)

Folder Structure:

.gemini/
settings.json
gemini.md
main.py
pyproject.toml
README.md
.env
uv.lock

Functional Architecture:

PDF Upload:
Accepts PDF files and shows a preview of extracted text (first 2,000 characters).

Text Processing:
Extracts text from PDF using PyPDF2 and cleans it by removing extra spaces and artifacts.

AI Agent:
Uses Gemini via OpenAgents SDK to summarize text and generate quizzes (MCQs and reasoning questions). Converts agent output into a readable format.

UI Display:
Scrollable summary and quiz containers, optional Light/Dark toggle, modern card-style layout.

Flow:
User uploads PDF → Text is extracted and cleaned → Agent generates summary → Agent generates quiz → Streamlit UI displays summary and quiz

Example End-to-End User Flow:

User uploads "Chapter 3 – Neuroanatomy.pdf".

Text extraction occurs using PyPDF2.

Agent receives text and produces a summary containing key points, definitions, and concepts.

Quiz is generated containing MCQs and reasoning questions.

UI displays scrollable summary and quiz card with answers hidden.

Testing Scenarios:

Small PDFs → Summary + quiz instantly

Large PDFs (50 pages) → Summary concise, quiz accurate

Complex formatting → Cleaned text output

Repeated uploads → Session state resets cleanly

Missing PDFs → Graceful stop

Unique Improvements Over Original Version:

Fully architected like an enterprise AI system

Single-file structure (main.py)

Standardized agent prompt and workflow

Async agent calls for smooth performance

Clean abstraction boundaries

Ready-to-implement, production-ready code

Minimal zero-bloat design

Easy to extend for future features (memory, RAG, streaming)

Next Steps / Options:

Run main.py directly in Streamlit

Add Light/Dark mode and card-style UI

Extend the agent to handle multiple PDFs and caching.



