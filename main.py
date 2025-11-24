import os
import asyncio
import pypdf
import streamlit as st

from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI

# ---------------------------------------------------
# API Key Setup (Streamlit Secrets or .env)
# ---------------------------------------------------
if hasattr(st, "_is_running_with_streamlit") and st._is_running_with_streamlit:
    # Running on Streamlit Cloud
    API_KEY = st.secrets.get("GEMINI_API_KEY")
else:
    # Local VS Code
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

if not API_KEY:
    st.error("❌ GEMINI_API_KEY missing! Add it to .env (local) or Streamlit Secrets (cloud).")
    st.stop()

# ---------------------------------------------------
# PDF Extractor (UI)
# ---------------------------------------------------
def extract_pdf_text_normal(file_path: str) -> str:
    """Extract text from PDF pages for UI."""
    text = []
    with open(file_path, "rb") as pdf:
        reader = pypdf.PdfReader(pdf)
        for pg in reader.pages:
            text.append(pg.extract_text() or "")
    return "\n".join(text)

# ---------------------------------------------------
# Agent Tool (PDF Extractor)
# ---------------------------------------------------
@function_tool
def extract_pdf_text(file_path: str) -> str:
    """Tool version of PDF extractor for Gemini."""
    return extract_pdf_text_normal(file_path)

# ---------------------------------------------------
# Agent Setup
# ---------------------------------------------------
@st.cache_resource
def get_agent():
    client = AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=client
    )

    return Agent(
        model=model,
        name="StudyNotesAI",
        instructions=(
            "You are an AI Study Assistant.\n"
            "1️⃣ Generate a structured summary.\n"
            "2️⃣ Extract key learning points.\n"
            "3️⃣ Create a quiz (MCQs + short questions).\n"
            "Make everything neat, organized, and easy to study."
        ),
        tools=[extract_pdf_text],
    )

# ---------------------------------------------------
# Async Runner
# ---------------------------------------------------
async def run_agent(agent, text):
    return await Runner.run(
        starting_agent=agent,
        input=f"Create summary, key points, and quiz from this text:\n\n{text}"
    )

# ---------------------------------------------------
# Custom UI Styling
# ---------------------------------------------------
def load_custom_css():
    st.markdown("""
        <style>
            body {
                font-family: 'Inter', sans-serif;
            }

            .title-container {
                background: linear-gradient(135deg, #3b82f6, #8b5cf6);
                padding: 25px;
                border-radius: 20px;
                color: white;
                text-align: center;
                margin-bottom: 20px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            }

            .glass-card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(10px);
                padding: 20px;
                border-radius: 15px;
                border: 1px solid rgba(255,255,255,0.25);
                margin-bottom: 25px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.10);
            }

            .stButton>button {
                width: 100%;
                padding: 12px;
                border-radius: 10px;
                font-size: 16px;
                background: linear-gradient(135deg, #2563eb, #7c3aed);
                color: white;
                border: none;
                transition: 0.3s ease;
            }

            .stButton>button:hover {
                transform: scale(1.02);
                background: linear-gradient(135deg, #1d4ed8, #6d28d9);
            }
        </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# Streamlit UI
# ---------------------------------------------------
def run_streamlit_app():
    st.set_page_config(page_title="AI PDF Study Assistant", layout="wide")
    load_custom_css()

    # Title
    st.markdown("""
        <div class="title-container">
            <h1>📘 AI PDF Study Assistant</h1>
            <p>Upload a PDF → Get Summary → Key Points → Quiz</p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📄 Upload a PDF file", type=["pdf"])

    if uploaded_file:
        # ==============================
        # PDF Upload + Extraction Card
        # ==============================
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        temp_folder = "temp_uploads"
        os.makedirs(temp_folder, exist_ok=True)

        file_path = os.path.join(temp_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("PDF uploaded successfully ✔")

        pdf_text = extract_pdf_text_normal(file_path)
        st.subheader("📄 Extracted Text from PDF")
        st.text_area("Raw PDF Content", pdf_text, height=320)

        st.markdown('</div>', unsafe_allow_html=True)

        # ==============================
        # AI Generation Card
        # ==============================
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        agent = get_agent()

        if st.button("✨ Generate Summary + Key Points + Quiz"):
            st.info("⏳ Processing your PDF... Please wait.")

            try:
                # Run async safely
                result = asyncio.run(run_agent(agent, pdf_text))
                st.success("🎉 Completed Successfully!")
                st.subheader("📝 Summary + Key Points + Quiz")
                st.write(result.final_output)
            except Exception as e:
                st.error("❌ An error occurred.")
                st.exception(e)

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Main Entry
# ---------------------------------------------------
if __name__ == "__main__":
    run_streamlit_app()
