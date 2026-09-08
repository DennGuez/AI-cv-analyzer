import streamlit as st
from state import init_state
from ui.input_section import render_input
from ui.results import render_results_area


def main():
    """Punto de entrada: configura la página y orquesta las dos columnas."""
    st.set_page_config(
        page_title="Sistema de Evaluación de CVs",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    init_state()

    st.title("📄 Sistema de Evaluación de CVs con IA")
    st.markdown("""
    **Analiza currículums y evalúa candidatos de manera objetiva usando IA**

    Este sistema utiliza inteligencia artificial para:
    - Extraer información clave de currículums en PDF
    - Analizar la experiencia y habilidades del candidato
    - Evaluar el ajuste al puesto específico
    - Proporcionar recomendaciones objetivas de contratación
    """)
    st.divider()

    col_entrada, col_resultado = st.columns([1, 1], gap="large")
    with col_entrada:
        render_input()
    with col_resultado:
        render_results_area()


if __name__ == "__main__":
    main()
