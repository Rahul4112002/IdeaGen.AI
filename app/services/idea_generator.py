import os
from groq import Groq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class IdeaGeneratorService:
    """Service to generate startup ideas using Groq Llama-3"""
    
    def __init__(self):
        # Initialize Groq client with API key from .env file
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )
        # Set the model name (Llama 3)
        self.model = "llama-3.3-70b-versatile"
        
        # Create a prompt template using LangChain
        self.prompt_template = PromptTemplate(
            input_variables=["interests"],
            template="""
You are an expert startup advisor and idea generator. Based on the user's interests, generate a unique and viable startup idea.

User Interests: {interests}

Provide the response EXACTLY in the following format with clear sections:

IDEA TITLE:
[A catchy, innovative name for the startup - keep it concise and memorable]

PROBLEM STATEMENT:
[Describe the specific problem this startup solves in 2-3 clear sentences. Be detailed and specific about the pain point.]

SOLUTION:
[Explain how this startup solves the problem in 3-4 sentences. Include:
- Core features and functionality
- Unique approach or technology used
- Key benefits to users]

TARGET AUDIENCE:
[Define the primary users/customers in 2-3 sentences. Include:
- Demographics (age, profession, location)
- Specific characteristics and needs
- Why they would use this product]

MARKET POTENTIAL:
[Explain the market opportunity in 2-3 sentences. Include:
- Market size and growth trends
- Why there is demand now
- Competitive advantages]

Make sure each section is clearly labeled and the idea is innovative, practical, and addresses a real market need.
"""
        )
        
    def generate_idea(self, interests: str) -> dict:
        """
        Generate a startup idea based on user interests
        
        Args:
            interests: User's interests as a string
            
        Returns:
            Dictionary containing parsed startup idea components
        """
        try:
            # Format the prompt with user's interests
            formatted_prompt = self.prompt_template.format(
                interests=interests
            )
            
            # Call Groq API to generate completion
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful startup advisor."
                    },
                    {
                        "role": "user",
                        "content": formatted_prompt
                    }
                ],
                model=self.model,
                temperature=0.8,  # Higher temperature = more creative responses
                max_tokens=1000   # Maximum length of response
            )
            
            # Extract the AI's response
            response_text = chat_completion.choices[0].message.content
            
            # Parse the response into structured format
            parsed_idea = self._parse_response(response_text)
            
            return parsed_idea
            
        except Exception as e:
            # If something goes wrong, raise an error
            raise Exception(f"Error generating idea: {str(e)}")
        
    def _parse_response(self, response: str) -> dict:
        """
        Parse the AI response into structured components
        
        Args:
            response: Raw text response from AI
            
        Returns:
            Dictionary with separated components
        """
        # Split response by keywords
        sections = {
            "idea_title": "",
            "problem_statement": "",
            "solution": "",
            "target_audience": "",
            "market_potential": ""
        }
        
        try:
            # Clean up the response
            response = response.strip()
            
            # Extract each section using string operations
            if "IDEA TITLE:" in response:
                start = response.find("IDEA TITLE:") + len("IDEA TITLE:")
                end = response.find("\n\nPROBLEM STATEMENT:")
                if end == -1:
                    end = response.find("PROBLEM STATEMENT:")
                sections["idea_title"] = response[start:end].strip()
            
            if "PROBLEM STATEMENT:" in response:
                start = response.find("PROBLEM STATEMENT:") + len("PROBLEM STATEMENT:")
                end = response.find("\n\nSOLUTION:")
                if end == -1:
                    end = response.find("SOLUTION:")
                sections["problem_statement"] = response[start:end].strip()
            
            if "SOLUTION:" in response:
                start = response.find("SOLUTION:") + len("SOLUTION:")
                end = response.find("\n\nTARGET AUDIENCE:")
                if end == -1:
                    end = response.find("TARGET AUDIENCE:")
                sections["solution"] = response[start:end].strip()
            
            if "TARGET AUDIENCE:" in response:
                start = response.find("TARGET AUDIENCE:") + len("TARGET AUDIENCE:")
                end = response.find("\n\nMARKET POTENTIAL:")
                if end == -1:
                    end = response.find("MARKET POTENTIAL:")
                sections["target_audience"] = response[start:end].strip()
            
            if "MARKET POTENTIAL:" in response:
                start = response.find("MARKET POTENTIAL:") + len("MARKET POTENTIAL:")
                sections["market_potential"] = response[start:].strip()
                
            # If any section is empty, try alternative parsing
            if not all(sections.values()):
                # Print response for debugging
                print("DEBUG: Raw AI Response:")
                print(response)
                print("DEBUG: Parsed sections:")
                print(sections)
                
        except Exception as e:
            # If parsing fails, return the whole response in problem_statement
            print(f"Parsing error: {str(e)}")
            sections["idea_title"] = "Generated Idea"
            sections["problem_statement"] = response
        
        return sections
    