from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title="Teralink Chatbot API",
    description="Core chatbot and public API of the Teralink AI assistant ecosystem.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.app_env}