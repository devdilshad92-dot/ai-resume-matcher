import io
import logging
from pypdf import PdfReader

logger = logging.getLogger(__name__)


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
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        return ""
