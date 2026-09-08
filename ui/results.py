import json
import time
import streamlit as st
from models.cv_model import AnalysisCV
from services.cv_analysis import cv_analysis


def render_results_area():
    """Dibuja la columna derecha. Ejecuta el análisis una sola vez y lo cachea."""
    st.header("📊 Resultado del Análisis")

    # 'analizar' es un disparador de un solo uso
    if st.session_state.get("analizar"):
        st.session_state["analizar"] = False  # se consume aquí
        archivo_cv = st.session_state.get("archivo_cv")
        descripcion = (st.session_state.get("descripcion_puesto") or "").strip()

        if archivo_cv is None:
            st.error("⚠️ Por favor sube un archivo PDF con el currículum")
        elif not descripcion:
            st.error("⚠️ Por favor proporciona una descripción detallada del puesto")
        else:
            # with st.spinner("🔄 Procesando currículum..."):
                try:
                    st.session_state["resultado"] = _analizar_con_progreso(archivo_cv, descripcion)
                except ValueError as e:
                    st.error(f"❌ {e}")
                    st.session_state["resultado"] = None

    resultado = st.session_state.get("resultado")
    if resultado:
        mostrar_resultados(resultado)
    else:
        _mostrar_instrucciones()


def mostrar_resultados(resultado: AnalysisCV):
    """Muestra los resultados de forma estructurada."""
    st.subheader("🎯 Evaluación Principal")

    if resultado.fit_score >= 80:
        color, nivel, mensaje = "🟢", "EXCELENTE", "Candidato altamente recomendado"
    elif resultado.fit_score >= 60:
        color, nivel, mensaje = "🟡", "BUENO", "Candidato recomendado con reservas"
    elif resultado.fit_score >= 40:
        color, nivel, mensaje = "🟠", "REGULAR", "Candidato requiere evaluación adicional"
    else:
        color, nivel, mensaje = "🔴", "BAJO", "Candidato no recomendado"

    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.metric("Porcentaje de Ajuste al Puesto",
            f"{resultado.fit_score}%", delta=f"{color} {nivel}")
        st.markdown(f"**{mensaje}**")

    st.divider()
    st.subheader("👤 Perfil del Candidato")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**👨‍💼 Nombre:** {resultado.candidate_name}")
        st.info(f"**⏱️ Experiencia:** {resultado.years_of_experience} años")
    with col2:
        st.info(f"**🎓 Educación:** {resultado.education}")

    st.subheader("💼 Experiencia Relevante")
    st.info(f"📋 **Resumen:**\n\n{resultado.relevant_experience}")

    st.divider()
    st.subheader("🛠️ Habilidades Técnicas Clave")
    if resultado.key_skills:
        cols = st.columns(min(len(resultado.key_skills), 4))
        for i, habilidad in enumerate(resultado.key_skills):
            with cols[i % 4]:
                st.success(f"✅ {habilidad}")
    else:
        st.warning("No se identificaron habilidades técnicas específicas")

    st.divider()
    col_fort, col_mej = st.columns(2)
    with col_fort:
        st.subheader("💪 Fortalezas Principales")
        for i, f in enumerate(resultado.streghts or [], 1):
            st.markdown(f"**{i}.** {f}")
    with col_mej:
        st.subheader("📈 Áreas de Desarrollo")
        for i, a in enumerate(resultado.development_areas or [], 1):
            st.markdown(f"**{i}.** {a}")

    st.divider()
    st.subheader("📋 Recomendación Final")
    if resultado.fit_score >= 70:
        st.success("✅ **CANDIDATO RECOMENDADO** — Proceder con las siguientes etapas.")
    elif resultado.fit_score >= 50:
        st.warning("⚠️ **CANDIDATO CON POTENCIAL** — Requiere entrevista técnica.")
    else:
        st.error("❌ **CANDIDATO NO RECOMENDADO** — Continuar la búsqueda.")

    # 💾 Guardar ahora SÍ funciona: descarga un JSON con el análisis
    st.markdown("---")
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        datos = {
            "candidato": resultado.candidate_name,
            "fit_score": resultado.fit_score,
            "experiencia_anios": resultado.years_of_experience,
            "educacion": resultado.education,
            "habilidades": resultado.key_skills,
            "fortalezas": resultado.streghts,
            "areas_desarrollo": resultado.development_areas,
        }
        st.download_button(
            "💾 Guardar Análisis",
            data=json.dumps(datos, ensure_ascii=False, indent=2),
            file_name=f"analisis_{resultado.candidate_name}.json",
            mime="application/json",
            use_container_width=True,
        )


def _mostrar_instrucciones():
    st.info("""
    👆 **Instrucciones:**

    1. Sube un CV en formato PDF en la columna izquierda
    2. Describe detalladamente el puesto de trabajo
    3. Haz clic en "Analizar Candidato"
    4. Aquí aparecerá el análisis completo

    **Consejos:** usa CVs con texto seleccionable (no escaneados) y sé específico en el puesto.
    """)

def _analizar_con_progreso(archivo_cv, descripcion):
    """Ejecuta el análisis mostrando una barra con mensajes por etapas."""
    barra = st.progress(0)
    estado = st.empty()

    etapas = [
        (15, "📄 Extrayendo texto del CV..."),
        (35, "🔍 Identificando datos del candidato..."),
        (55, "🧠 Analizando experiencia y habilidades..."),
        (80, "📊 Evaluando ajuste al puesto..."),
    ]
    for porcentaje, mensaje in etapas:
        estado.markdown(f"**{mensaje}**")
        barra.progress(porcentaje)
        time.sleep(0.5)   # pausa para que el mensaje se vea

    # 👇 aquí ocurre el trabajo real (la barra se queda en 80% mientras)
    resultado = cv_analysis(archivo_cv, descripcion)

    estado.markdown("**✅ Análisis completado**")
    barra.progress(100)
    time.sleep(0.4)

    # limpiamos la barra y el mensaje
    barra.empty()
    estado.empty()
    return resultado
