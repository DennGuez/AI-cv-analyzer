import pytest
from unittest.mock import patch, MagicMock

# Importación correcta desde la raíz del proyecto
from services.cv_analysis import cv_analysis
from models.cv_model import AnalysisCV 

# --- TEST 1: Caso cuando el CV es ilegible ---
@patch('services.cv_analysis.extract_cv_text')
def test_cv_analysis_ilegible(mock_extract):
    """Prueba que si el texto extraído falla, devuelve el objeto AnalysisCV por defecto."""
    mock_extract.return_value = ""
    
    resultado = cv_analysis("archivo_falso.pdf", "Senior Python Developer")
    
    assert isinstance(resultado, AnalysisCV)
    assert resultado.candidate_name == "CV ilegible"
    assert resultado.fit_score == 0
    assert "No se pudo leer el PDF" in resultado.relevant_experience


# --- TEST 2: Caso cuando la IA responde correctamente ---
@patch('services.cv_analysis.cv_evaluator')
@patch('services.cv_analysis.extract_cv_text')
def test_cv_analysis_exito(mock_extract, mock_evaluator):
    """Prueba el camino feliz: la IA procesa el texto correctamente."""
    mock_extract.return_value = "Experiencia: 5 años en Python..."
    
    mock_chain = MagicMock()
    mock_chain.invoke.return_value = AnalysisCV(
        candidate_name="Juan Pérez",
        years_of_experience=5,
        key_skills=["Python", "FastAPI"],
        education="Ingeniero",
        relevant_experience="5 años en backend",
        streghts=["Autónomo"],
        development_areas=["Vue"],
        fit_score=85,
    )
    mock_evaluator.return_value = mock_chain

    resultado = cv_analysis("archivo_valido.pdf", "Python Developer")

    assert resultado.candidate_name == "Juan Pérez"
    assert resultado.fit_score == 85
    assert "Python" in resultado.key_skills


# --- TEST 3: Caso cuando la API de la IA falla ---
@patch('services.cv_analysis.cv_evaluator')
@patch('services.cv_analysis.extract_cv_text')
def test_cv_analysis_error_ia(mock_extract, mock_evaluator):
    """Prueba que si la IA lanza un error inesperado, la app no se rompe."""
    mock_extract.return_value = "Texto del CV válido"
    
    mock_chain = MagicMock()
    mock_chain.invoke.side_effect = Exception("API Key inválida")
    mock_evaluator.return_value = mock_chain

    resultado = cv_analysis("archivo.pdf", "Cualquier puesto")

    assert resultado.candidate_name == "Error al procesar CV"
    assert resultado.fit_score == 0
