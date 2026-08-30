from contextlib import asynccontextmanager
from fastapi import FastAPI

from services.pdf_converter_factory import build_pdf_converter
from routers import pdf_converter

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pdf_converter = await build_pdf_converter()
    yield
    await app.state.pdf_converter.close()

app = FastAPI(lifespan=lifespan)
app.include_router(pdf_converter.router)
