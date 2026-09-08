import streamlit as st


def render_input():
    """Dibuja la columna izquierda: carga de CV, descripción y botones."""
    st.header("📋 Datos de Entrada")

    st.file_uploader(
        "**1. Sube el CV del candidato (PDF)**",
        type=["pdf"],
        key="archivo_cv",   # 👈 con key, el estado se maneja solo
        help="Selecciona un PDF con el currículum. El texto debe ser legible (no imagen).",
    )

    archivo = st.session_state.get("archivo_cv")
    if archivo is not None:
        st.success(f"✅ Archivo cargado: {archivo.name}")
        st.info(f"📊 Tamaño: {archivo.size:,} bytes")

    st.markdown("---")
    st.markdown("**2. Descripción del puesto de trabajo**")
    st.text_area(
        "Detalla los requisitos, responsabilidades y habilidades necesarias:",
        height=250,
        key="descripcion_puesto",   # 👈 idem
        placeholder="Ej: Desarrollador Frontend Senior, 3+ años con React...",
        help="Sé específico sobre requisitos técnicos, experiencia y responsabilidades.",
    )

    st.markdown("---")
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("🔍 Analizar Candidato", type="primary", use_container_width=True):
            st.session_state["analizar"] = True   # 👈 solo lo activamos, no lo machacamos
    with col_btn2:
        if st.button("🗑️ Limpiar", use_container_width=True):
            _limpiar()


def _limpiar():
    """Borra el estado para dejar el formulario vacío de verdad."""
    for k in ["archivo_cv", "descripcion_puesto", "analizar", "resultado"]:
        st.session_state.pop(k, None)
    st.rerun()
