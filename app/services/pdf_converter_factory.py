from app.services.pdf_converter import PdfConverter
from app.services.chromium_converter import ChromiumConverter

async def build_pdf_converter() -> PdfConverter:
    pdf_converter = ChromiumConverter()
    await pdf_converter.create()
    return pdf_converter