"""
main.py

Main FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.routes import router as api_router

app = FastAPI(
    title="JSO Agent",
    description="AI Job Search Agent powered by Groq",
    version="1.0"
)

# Register API routes
app.include_router(api_router, prefix="/api")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def home():
    """
    Serve the frontend page.
    """
    return FileResponse("app/static/index.html")