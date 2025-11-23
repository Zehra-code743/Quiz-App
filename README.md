# 📖 Study Notes & Quiz Generator – AI-Powered Learning from PDFs

Transform your PDFs into **interactive study material** with this **Streamlit-powered application**. Upload any academic PDF, and a **Gemini-powered AI agent** will generate **structured study notes** and a **ready-to-use quiz** in seconds. Perfect for students, educators, and lifelong learners!  

---

## ⚡ Quick Start

1. **Install Dependencies**  
```bash
pip install -r requirements.txt
Set Your Gemini API Key
Create a .env file at the project root:

ini
Copy code
GEMINI_API_KEY="YOUR_API_KEY"
Run the App

bash
Copy code
streamlit run main.py
Upload a PDF and Start Learning
Drag and drop any PDF, and watch the AI generate notes and a quiz instantly.

🤖 How It Works
PDF Upload: Drop your PDF into the app.

Text Extraction: PyPDF2 extracts all readable content.

AI-Powered Summarization: A Gemini agent reads the text, condenses it into clear, structured study notes, and produces an assessment-ready quiz.

Interactive UI: Notes and quizzes appear in a scrollable, user-friendly Streamlit interface. Light/Dark mode lets you study comfortably anytime.

🌟 Key Features
Instant Study Notes: Summarizes chapters, definitions, and key concepts automatically.

Quiz Generator: Multiple-choice and reasoning questions created from your PDF content.

Beautiful Interface: Scrollable sections, clean design, and Light/Dark mode.

Minimal, Zero-Bloat: Only the essentials—fast, efficient, and production-ready.

Async Processing: Handles large PDFs smoothly without lag.

🎯 Benefits
Saves hours of manual note-taking

Reinforces learning with quizzes immediately

Ideal for exam prep, research, or knowledge review

Turn any PDF into an interactive study tool in seconds

🚀 Future Enhancements
Multi-PDF support for batch processing

Answer reveal, scoring, and progress tracking

Highlighting and PDF content search

Advanced AI features: linking concepts and reasoning explanations
