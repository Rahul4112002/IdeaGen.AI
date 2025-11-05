from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os

# Import our custom models and service
from app.schemas.models import InterestsInput, StartupIdea
from app.services.idea_generator import IdeaGeneratorService

# Create FastAPI application instance
app = FastAPI(
    title="IdeaGen.AI",
    description="AI-powered Startup Idea Generator",
    version="1.0.0"
)

# Set up templates folder for HTML files
templates = Jinja2Templates(directory="app/templates")

# Initialize the idea generator service
idea_service = IdeaGeneratorService()

# Root endpoint - serves the homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the homepage"""
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint to generate startup ideas
@app.post("/generate", response_model=StartupIdea)
async def generate_startup_idea(input_data: InterestsInput):
    """
    Generate a startup idea based on user interests
    
    Args:
        input_data: User's interests input
        
    Returns:
        StartupIdea object with all generated components
    """
    try:
        # Validate that interests field is not empty
        if not input_data.interests or len(input_data.interests.strip()) == 0:
            raise HTTPException(
                status_code=400, 
                detail="Please provide your interests"
            )
        
        # Call the AI service to generate idea
        idea = idea_service.generate_idea(input_data.interests)
        
        # Return the generated idea
        return StartupIdea(**idea)
        
    except Exception as e:
        # If error occurs, return error message
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    """Check if API is running"""
    return {"status": "healthy", "service": "IdeaGen.AI"}
