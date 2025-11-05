from pydantic import BaseModel
from typing import List

# This is the input model - what user sends to us
class InterestsInput(BaseModel):
    interests: str  # User's interests as a text string
    
    class Config:
        # Example of how the input should look
        json_schema_extra = {
            "example": {
                "interests": "AI, Healthcare, Mobile Apps"
            }
        }

# This is the output model - what we send back to user
class StartupIdea(BaseModel):
    idea_title: str  # Name of the startup idea
    problem_statement: str  # What problem does it solve
    solution: str  # How it solves the problem
    target_audience: str  # Who will use this product
    market_potential: str  # Is there demand for this
