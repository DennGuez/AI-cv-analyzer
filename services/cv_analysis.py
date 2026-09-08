from langchain_openai import ChatOpenAI
from models.cv_model import AnalysisCV
from prompts.cv_prompts import create_prompts_system
from services.pdf_processor import extract_cv_text  


def cv_evaluator():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    structured_model = llm.with_structured_output(AnalysisCV)
    chat_prompt = create_prompts_system()
    chain = chat_prompt | structured_model
    return chain


def cv_analysis(pdf_file, job_description: str) -> AnalysisCV:
    cv_text = extract_cv_text(pdf_file)

    # Si el PDF es ilegible/imagen, cortamos antes de llamar al modelo
    if not cv_text or cv_text.startswith("Error"):
        return AnalysisCV(
            candidate_name="CV ilegible",
            years_of_experience=0,
            key_skills=[],
            education="No especificado",
            relevant_experience="No se pudo leer el PDF (posible imagen sin OCR)",
            streghts=[],
            development_areas=[],
            fit_score=0,
        )

    try:
        chain = cv_evaluator()
        return chain.invoke({
            "cv_text": cv_text,
            "job_description": job_description,
        })
    except Exception as e:
        print(f"[cv_analysis] Error: {e}")
        return AnalysisCV(
            candidate_name="Error al procesar CV",
            years_of_experience=0,
            key_skills=[],
            education="No especificado",
            relevant_experience="No especificado",
            streghts=[],
            development_areas=[],
            fit_score=0,
        )
