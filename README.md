# 🤖 AI-Powered CV Evaluation System

An **AI-driven** web app built with Streamlit that analyzes PDF resumes and evaluates how well a candidate fits a given job. Powered by **OpenAI (gpt-4o-mini)** and **LangChain**, it extracts the candidate profile, highlights strengths and gaps, and scores the fit for the role.

## ✨ Features

- 📤 Upload a CV in PDF format
- 📝 Free-text job description
- 🤖 **Automated AI analysis** — data extraction + evaluation
- 🎯 Job-fit score (0–100) with visual level (Excellent / Good / Fair / Low)
- 👤 Profile extraction: name, experience, education, skills
- 💪 Strengths and areas for improvement
- 📋 Final hiring recommendation
- 💾 Export the analysis as JSON

## 🛠️ Tech Stack

- **OpenAI (gpt-4o-mini)** — the AI language model at the core
- **LangChain** — prompt orchestration and structured output
- **Streamlit** — web interface
- **pdfplumber** — PDF text extraction
- **Pydantic** — structured output validation

## ⚙️ How It Works

1. **Extraction** — pdfplumber pulls the text from the PDF.
2. **AI Analysis** — the resume text and job description are sent to gpt-4o-mini through a specialized prompt.
3. **Structured Output** — LangChain forces the model's response into the `AnalysisCV` (Pydantic) schema for consistent data.
4. **Display** — Streamlit renders the result in a clean, organized view.

## 📁 Project Structure

```
project/
├── streamlit_ui.py           # UI (main)
├── models/
│   └── cv_model.py           # AnalysisCV Pydantic model
├── services/
│   ├── pdf_processor.py      # PDF text extraction
│   └── cv_evaluator.py       # AI analysis chain
├── prompts/
│   └── cv_prompts.py         # System & analysis prompts
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone <repo-url>
cd project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

**Requirements:** Python 3.10+ and an OpenAI API key.

## 🔑 Configuration

Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY=your_key_here
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

## ▶️ Usage

```bash
streamlit run streamlit_ui.py
```

It opens in your browser (default: `http://localhost:8501`). Then upload a PDF CV, enter the job description, click **"Analyze Candidate"**, review the results, and download if needed.

## ⚠️ Limitations

- Only processes PDFs with selectable text; scanned/image resumes need OCR.
- AI evaluation is a decision-support tool, not a final verdict.

## 🔮 Roadmap

- OCR support for scanned CVs
- Export analysis as PDF/TXT
- Evaluation history
- Multi-candidate comparison

## 📄 License

MIT
