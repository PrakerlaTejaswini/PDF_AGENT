# 📄 AI PDF Q&A Agent using Gemini

An intelligent PDF Question & Answer application built with **Streamlit** and **Google Gemini AI**. The application allows users to upload a PDF document, ask questions, and receive accurate answers. It also uses a simple AI Agent to decide whether to **search**, **summarize**, or **directly answer** the user's query.

---

## 🚀 Features

- 📄 Upload any PDF document
- 🤖 AI Agent decides the best action:
  - SEARCH
  - SUMMARIZE
  - ANSWER
- 🔍 Question Answering from PDF
- 📝 PDF Summarization
- ⚡ Powered by Google Gemini 2.5 Flash
- 🎨 Simple Streamlit User Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

---

## 📂 Project Structure

```
AI-PDF-QA-Agent/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-PDF-QA-Agent.git

cd AI-PDF-QA-Agent
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file inside the project folder.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

> **Note:** Never upload your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 How It Works

### Step 1
Upload a PDF document.

### Step 2
Enter a question related to the PDF.

### Step 3
The AI Agent analyzes the query and selects one of the following actions:

- **SEARCH** → Searches the uploaded PDF for relevant information.
- **SUMMARIZE** → Generates a summary of the uploaded PDF.
- **ANSWER** → Provides a direct answer using Gemini.

### Step 4
Gemini generates the final response.

---

## 🧠 Agent Workflow

```
                User
                  │
                  ▼
        Upload PDF & Question
                  │
                  ▼
          AI Agent Decision
      ┌─────────┼─────────┐
      │         │         │
      ▼         ▼         ▼
   SEARCH   SUMMARIZE   ANSWER
      │         │         │
      └─────────┼─────────┘
                ▼
        Gemini 2.5 Flash
                │
                ▼
         Display Response
```

---

## 📦 Requirements

```
streamlit
google-generativeai
PyPDF2
python-dotenv
```

Or install using:

```bash
pip install -r requirements.txt
```

---

## 📸 Application Preview

- Upload PDF
- Ask Questions
- View Agent Decision
- Get AI-Generated Answer

---

## 🔒 Security

- Store API keys in a `.env` file.
- Add `.env` to `.gitignore`.
- Never commit API keys to GitHub.

Example `.gitignore`

```
.env
__pycache__/
*.pyc
```

---

## 🌟 Future Enhancements

- RAG (Retrieval-Augmented Generation)
- ChromaDB Integration
- FAISS Vector Store
- Chat History
- Multi-PDF Support
- Conversation Memory
- PDF Highlighting
- Voice Input
- Download Chat History

---

## 👩‍💻 Author

**Tejaswini Prakerla**

GitHub: https://github.com/PrakerlaTejaswini

---

## 📄 License

This project is licensed under the MIT License.
