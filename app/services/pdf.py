import io
from pypdf import PdfReader


def extract_text(file_bytes: bytes) -> str:
    """
    Extract text from a PDF file.
    """
    try:
        pdf_stream = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception:
        return ""
