# import streamlit as st
# import google.generativeai as genai
# from PyPDF2 import PdfReader
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Configure Gemini
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-2.5-flash")

# # Streamlit UI
# st.set_page_config(page_title="AI PDF Q&A Agent", layout="centered")
# st.title("📄 AI PDF Q&A Agent (Gemini)")
# st.write("Upload a PDF and ask questions. The agent decides how to answer.")

# # Upload PDF
# uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# pdf_text = ""

# if uploaded_file:
#     reader = PdfReader(uploaded_file)
#     for page in reader.pages:
#         pdf_text += page.extract_text()

#     st.success("PDF uploaded successfully!")

# # User question
# question = st.text_input("Ask a question from the PDF")

# # -------- AGENT LOGIC -------- #
# def agent_decision(question):
#     """
#     Decide whether to search, summarize, or answer directly
#     """
#     prompt = f"""
#     You are an AI agent.
#     Decide the action for the user's question:
#     - SEARCH: If specific info is needed
#     - SUMMARIZE: If summary is requested
#     - ANSWER: If direct answer possible

#     Question: {question}

#     Respond with only one word:
#     SEARCH or SUMMARIZE or ANSWER
#     """
#     response = model.generate_content(prompt)
#     return response.text.strip()

# def search_pdf(question, pdf_text):
#     prompt = f"""
#     Use the following PDF content to answer the question.

#     PDF Content:
#     {pdf_text}

#     Question:
#     {question}
#     """
#     return model.generate_content(prompt).text

# def summarize_pdf(pdf_text):
#     prompt = f"Summarize the following PDF in simple words:\n{pdf_text}"
#     return model.generate_content(prompt).text

# def direct_answer(question):
#     return model.generate_content(question).text

# # Run Agent
# if st.button("Ask Agent"):
#     if not uploaded_file:
#         st.warning("Please upload a PDF first.")
#     elif not question:
#         st.warning("Please enter a question.")
#     else:
#         with st.spinner("Agent is thinking... 🤔"):
#             action = agent_decision(question)

#             st.write(f"🧠 **Agent Action:** `{action}`")

#             if action == "SEARCH":
#                 answer = search_pdf(question, pdf_text)
#             elif action == "SUMMARIZE":
#                 answer = summarize_pdf(pdf_text)
#             else:
#                 answer = direct_answer(question)

#             st.subheader("✅ Answer")
#             st.write(answer)




import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
from google.api_core.exceptions import DeadlineExceeded

# ------------------------------
# Load API Key
# ------------------------------
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------------------
# Streamlit UI
# ------------------------------

st.set_page_config(page_title="AI PDF Q&A Agent", layout="wide")

st.title("📄 AI PDF Q&A Agent")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

pdf_text = ""

if uploaded_file:

    reader = PdfReader(uploaded_file)

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pdf_text += text + "\n"

    # Limit size to avoid timeout
    pdf_text = pdf_text[:12000]

    st.success("✅ PDF Uploaded Successfully!")

question = st.text_input("Ask your question")

# ------------------------------
# Gemini Helper
# ------------------------------

def gemini_response(prompt):

    try:

        response = model.generate_content(
            prompt,
            request_options={"timeout": 120}
        )

        return response.text

    except DeadlineExceeded:

        return "⏳ Request timed out. Please upload a smaller PDF or ask a more specific question."

    except Exception as e:

        return f"Error: {e}"

# ------------------------------
# Agent Decision
# ------------------------------

def agent_decision(question):

    prompt = f"""
You are an intelligent AI Agent.

Decide the action.

SEARCH -> if information should be searched from PDF

SUMMARIZE -> if user asks summary

ANSWER -> general question

Question:
{question}

Return only one word.
"""

    action = gemini_response(prompt)

    return action.strip().upper()

# ------------------------------
# Search PDF
# ------------------------------

def search_pdf(question):

    prompt = f"""
Answer only from this PDF.

PDF:

{pdf_text}

Question:

{question}
"""

    return gemini_response(prompt)

# ------------------------------
# Summarize
# ------------------------------

def summarize_pdf():

    prompt = f"""
Summarize this PDF in simple bullet points.

PDF:

{pdf_text}
"""

    return gemini_response(prompt)

# ------------------------------
# Direct Answer
# ------------------------------

def direct_answer(question):

    return gemini_response(question)

# ------------------------------
# Ask Agent
# ------------------------------

if st.button("Ask Agent"):

    if uploaded_file is None:

        st.warning("Please upload a PDF.")

    elif question == "":

        st.warning("Enter a question.")

    else:

        with st.spinner("Thinking..."):

            action = agent_decision(question)

            st.info(f"Agent Decision : {action}")

            if "SEARCH" in action:

                answer = search_pdf(question)

            elif "SUMMARIZE" in action:

                answer = summarize_pdf()

            else:

                answer = direct_answer(question)

            st.subheader("Answer")

            st.write(answer)
