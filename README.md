# 📖 PDF STYUDY ASSISTANT & Quiz Generator – AI-Powered Learning from PDFs

Transform your PDFs into **interactive study material** with this **Streamlit-powered application**. Upload any academic PDF, and a **Gemini-powered AI agent** will generate **structured study notes** and a **ready-to-use quiz** in seconds. Perfect for students, educators, and lifelong learners!  

---

## ⚡ Quick Start

1. **Install Dependencies**  
```bash
pip install -r requirements.txt
Set Your Gemini API Key
Create a .env file at the project root and add:

ini
Copy code
GEMINI_API_KEY="YOUR_API_KEY"
Run the App

bash
Copy code
streamlit run main.py

## ⚡ Quick Start (Using VS Code + UV)

This project was originally created using **UV** for a clean, modern workflow.  
Below are the exact steps used for building the environment.

### **1️⃣ Create a new UV project**
```bash
uv init
2️⃣ Create & activate virtual environment
bash
Copy code
uv venv
Windows:

bash
Copy code
.venv\Scripts\activate
Mac/Linux:

bash
Copy code
source .venv/bin/activate
3️⃣ Install required packages using UV
bash
Copy code
uv add streamlit python-dotenv openai-agents pypdf

## 🤖 How It Works

- **PDF Upload:** Drop your PDF into the app.  
- **Text Extraction:** `PyPDF2` extracts all readable content.  
- **AI-Powered Summarization:** A **Gemini agent** reads the text, condenses it into **clear, structured study notes**, and produces an **assessment-ready quiz**.  
- **Interactive UI:** Notes and quizzes appear in a scrollable, user-friendly Streamlit interface. Light/Dark mode lets you study comfortably anytime.  

---

## 🌟 Key Features

- **Instant Study Notes:** Summarizes chapters, definitions, and key concepts automatically.  
- **Quiz Generator:** Multiple-choice and reasoning questions created from your PDF content.  
- **Beautiful Interface:** Scrollable sections, clean design, and Light/Dark mode.  
- **Minimal, Zero-Bloat:** Only the essentials—fast, efficient, and production-ready.  
- **Async Processing:** Handles large PDFs smoothly without lag.  

---

## 🎯 Benefits

- Saves hours of manual note-taking  
- Reinforces learning with quizzes immediately  
- Ideal for exam prep, research, or knowledge review  
- Turns any PDF into an interactive study tool in seconds  

---

## 🚀 Future Enhancements

- Multi-PDF support for batch processing  
- Answer reveal, scoring, and progress tracking  
- Highlighting and PDF content search  
- Advanced AI features: linking concepts and reasoning explanations  

---

## 📁 Folder Structure

.gemini/
settings.json
gemini.md
main.py
pyproject.toml
README.md
.env
uv.lock

## 🧠 How to Use

1. Open the project in **VS Code**  
2. Set up the environment (using **pip** or **uv**)  
3. Create and add your **.env** file  
4. Run the Streamlit app  
   ```bash
   streamlit run main.py



