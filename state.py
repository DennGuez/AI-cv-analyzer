import streamlit as st


def init_state():
    """Inicializa el estado de la sesión con valores por defecto."""
    st.session_state.setdefault("analizar", False)
    st.session_state.setdefault("resultado", None)
