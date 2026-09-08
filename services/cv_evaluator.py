
from langchain_openai import ChatOpenAI
from models.cv_model import AnalysisCV
from prompts.cv_prompts import create_prompts_system

def create_cv_evaluator():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    structured_model = llm.with_structured_output(AnalysisCV)
    chat_prompt = create_prompts_system()
    chain = chat_prompt | structured_model

    return chain

def evaluate_candidate(cv_text: str, job_description: str) -> AnalysisCV:
    try:
        evaluation_chain = create_cv_evaluator()
        result = evaluation_chain.invoke({
            "cv_text": cv_text,
            "job_description": job_description
        })
        return result
    except Exception as e:
        return AnalysisCV(
            candidate_name="Error al procesar CV",
            years_of_experience=0,
            key_skills=["Error al procesar CV"],
            education="Error al procesar CV",
            development_areas="Error al procesar CV",
            streghts=["Error al procesar CV"],
            relevant_experience="Error al procesar CV",
            fit_score=0
        )
    