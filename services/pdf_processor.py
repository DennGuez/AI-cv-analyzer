import pdfplumber

def extract_cv_text(pdf_file):
    try:
        pages = []
        with pdfplumber.open(pdf_file) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                text = (page.extract_text() or "").strip()
                if text:
                    pages.append(f"\n---- PAGE {i} ---\n{text}\n")

        full_text = "".join(pages).strip()
        return full_text or "Error: El PDF está vacío o es una imagen (necesita OCR)"

    except Exception as e:
        return f"Error al procesar el archivo PDF: {str(e)}"
