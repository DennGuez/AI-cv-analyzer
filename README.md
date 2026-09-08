# 📄 Sistema de Evaluación de CVs con IA

Aplicación web construida con **Streamlit** que analiza currículums en PDF y evalúa, mediante IA, qué tan bien se ajusta un candidato a un puesto de trabajo. Extrae el perfil del candidato, identifica fortalezas y áreas de mejora, y asigna un porcentaje de ajuste al puesto.

## ✨ Características

- 📤 Subida de CV en formato PDF
- 📝 Descripción libre del puesto a cubrir
- 🤖 Análisis automático con IA (extracción de datos + evaluación)
- 🎯 Porcentaje de ajuste al puesto (0–100) con nivel visual (Excelente / Bueno / Regular / Bajo)
- 👤 Extracción de perfil: nombre, experiencia, educación, habilidades
- 💪 Identificación de fortalezas y áreas de desarrollo
- 📋 Recomendación final de contratación
- 💾 Descarga del análisis en formato JSON

## 🛠️ Tecnologías

- **[Streamlit](https://streamlit.io/)** — interfaz web
- **[LangChain](https://python.langchain.com/)** — orquestación del prompt y salida estructurada
- **[OpenAI](https://platform.openai.com/)** (`gpt-4o-mini`) — modelo de lenguaje
- **[pdfplumber](https://github.com/jsvine/pdfplumber)** — extracción de texto del PDF
- **[Pydantic](https://docs.pydantic.dev/)** — validación de la salida estructurada

## 📁 Estructura del proyecto

```
proyecto/
├── streamlit_ui.py           # Interfaz de usuario (main)
├── models/
│   └── cv_model.py           # Modelo Pydantic AnalysisCV
├── services/
│   ├── pdf_processor.py      # Extracción de texto del PDF
│   └── cv_evaluator.py       # Cadena de análisis con IA
├── prompts/
│   └── cv_prompts.py         # Prompts del sistema y de análisis
├── requirements.txt
└── README.md
```

## 📋 Requisitos previos

- Python 3.10 o superior
- Una clave de API de OpenAI ([obtener aquí](https://platform.openai.com/api-keys))

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd proyecto
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuración

Crea un archivo `.env` en la raíz del proyecto con tu clave de OpenAI:

```
OPENAI_API_KEY=tu_clave_aqui
```

> ⚠️ No subas tu archivo `.env` al repositorio. Añádelo al `.gitignore`.

## ▶️ Uso

Lanza la aplicación con:

```bash
streamlit run streamlit_ui.py
```

Se abrirá en tu navegador (por defecto en `http://localhost:8501`). Después:

1. Sube el CV del candidato en formato PDF
2. Escribe la descripción del puesto
3. Pulsa **"Analizar Candidato"**
4. Revisa el análisis y descárgalo si lo necesitas

## ⚙️ Cómo funciona

1. **Extracción** — `pdfplumber` extrae el texto del PDF página por página.
2. **Análisis** — el texto y la descripción del puesto se envían a `gpt-4o-mini` a través de un prompt especializado.
3. **Salida estructurada** — LangChain fuerza la respuesta del modelo al esquema `AnalysisCV` (Pydantic), garantizando datos consistentes.
4. **Visualización** — Streamlit muestra el resultado de forma organizada.

## ⚠️ Limitaciones

- Solo procesa PDFs con **texto seleccionable**. Los CVs en formato imagen (escaneados o exportados como imagen) no se pueden leer sin OCR.
- La evaluación depende del modelo de IA y debe tomarse como apoyo, no como decisión final.

## 🔮 Posibles mejoras

- [ ] Soporte para OCR (CVs escaneados)
- [ ] Descarga del análisis en PDF o TXT
- [ ] Historial de candidatos evaluados
- [ ] Comparación entre varios candidatos

## 📄 Licencia

MIT