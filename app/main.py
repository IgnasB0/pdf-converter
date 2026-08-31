from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.services.pdf_converter_factory import build_pdf_converter
from app.routers import pdf_converter

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pdf_converter = await build_pdf_converter()
    yield
    await app.state.pdf_converter.close()

app = FastAPI(lifespan=lifespan)
app.include_router(pdf_converter.router)
