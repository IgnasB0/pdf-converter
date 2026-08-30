import binascii

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import base64

router = APIRouter()

class PdfConversionBody(BaseModel):
    base64_html: str

@router.post("/convert-to-pdf")
async def convert_to_pdf(body: PdfConversionBody, request: Request):
    pdf_converter = request.app.state.pdf_converter
    try:
        html_content = base64.b64decode(body.base64_html).decode()
    except (binascii.Error, UnicodeDecodeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid base64_html: {e}")

    pdf = await pdf_converter.convert_to_pdf(html_content)

    base64_Pdf = base64.b64encode(pdf).decode()

    return {"base64_pdf": base64_Pdf}