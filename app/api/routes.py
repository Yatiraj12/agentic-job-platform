"""
routes.py

Defines API routes for the Job Search Agent system.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.workflow import JobSearchWorkflow

router = APIRouter()

workflow = JobSearchWorkflow()


class JobRequest(BaseModel):
    query: str


@router.post("/search-jobs")
def search_jobs(request: JobRequest):
    """
    API endpoint to process job search requests.
    """

    result = workflow.run(request.query)

    return {
        "status": "success",
        "data": result
    }