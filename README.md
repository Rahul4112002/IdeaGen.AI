# 🧠 IdeaGen.AI - AI-Powered Startup Idea Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Groq](https://img.shields.io/badge/Groq-Llama3-orange.svg)

An intelligent web application that generates innovative startup ideas based on your interests using **Groq's Llama-3** AI model and **LangChain** framework.

---

## 🎥 Demo Video

> **[Watch the Demo Video Here](#)** *(

https://github.com/user-attachments/assets/d2a84f9d-c844-4594-a61e-1645d122c1cd





---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## ✨ Features

- 🤖 **AI-Powered Generation**: Leverages Groq's Llama-3 70B model for intelligent idea generation
- 🎯 **Personalized Ideas**: Generates startup ideas based on your specific interests
- 📊 **Structured Output**: Provides comprehensive startup plans with:
  - Catchy idea title
  - Problem statement
  - Solution description
  - Target audience analysis
  - Market potential insights
- 🎨 **Beautiful UI**: Modern, gradient-based interface with smooth animations
- ⚡ **Fast Response**: Powered by Groq's ultra-fast inference engine
- 🔄 **Real-time Generation**: Interactive loading states and error handling
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices

---

## 🛠️ Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server
- **[LangChain](https://www.langchain.com/)** - Framework for developing LLM applications
- **[Groq](https://groq.com/)** - AI inference platform with Llama-3 model
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation using Python type annotations

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (ES6+)** - Async/await API calls and DOM manipulation
- **Jinja2** - Template engine

### Other Tools
- **python-dotenv** - Environment variable management
- **Pydantic Settings** - Configuration management

---

## 📁 Project Structure

```
IdeaGen-AI/
│
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── schemas/
│   │   └── models.py           # Pydantic models for request/response
│   ├── services/
│   │   └── idea_generator.py  # AI idea generation service
│   └── templates/
│       └── index.html          # Frontend HTML template
│
├── .env                        # Environment variables (API keys)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- Groq API Key ([Get it here](https://console.groq.com/))

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/IdeaGen-AI.git
cd IdeaGen-AI
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** Get your free Groq API key from [https://console.groq.com/](https://console.groq.com/)

---

## ⚙️ Configuration

The application uses the following configuration:

- **AI Model**: `llama3-70b-8192` (Groq's Llama-3 70B)
- **Temperature**: `0.8` (Creative responses)
- **Max Tokens**: `1000`
- **Host**: `0.0.0.0` (All network interfaces)
- **Port**: `8000`

You can modify these settings in `app/services/idea_generator.py`.

---

## 💻 Usage

### Running the Application

1. **Activate your virtual environment** (if not already activated)

2. **Start the server:**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3. **Open your browser** and navigate to:

```
http://localhost:8000
```

or

```
http://127.0.0.1:8000
```

### Using the Application

1. Enter your interests in the input field (comma-separated)
   - Example: `AI, Healthcare, Mobile Apps, Education`

2. Click **"Generate Startup Idea ✨"**

3. Wait for the AI to generate your personalized startup idea

4. Review the comprehensive startup plan with:
   - 💡 **Idea Title**
   - ❓ **Problem Statement**
   - ✅ **Solution**
   - 🎯 **Target Audience**
   - 📈 **Market Potential**

---

## 🔌 API Endpoints

### `GET /`
- **Description**: Serves the homepage
- **Response**: HTML page

### `POST /generate`
- **Description**: Generates a startup idea based on user interests
- **Request Body**:
```json
{
  "interests": "AI, Healthcare, Mobile Apps"
}
```
- **Response**:
```json
{
  "idea_title": "HealthAI Companion",
  "problem_statement": "Many patients struggle to...",
  "solution": "HealthAI Companion is an AI-powered...",
  "target_audience": "Primary users include...",
  "market_potential": "The global digital health market..."
}
```

### `GET /health`
- **Description**: Health check endpoint
- **Response**:
```json
{
  "status": "healthy",
  "service": "IdeaGen.AI"
}
```

---

## 🧩 How It Works

1. **User Input**: User enters their interests through the web interface

2. **API Request**: Frontend sends a POST request to `/generate` endpoint

3. **Prompt Generation**: LangChain formats a structured prompt with user interests

4. **AI Processing**: Groq's Llama-3 model generates a comprehensive startup idea

5. **Response Parsing**: The service parses the AI response into structured sections

6. **Display**: Frontend displays the idea in an organized, visually appealing format

### Architecture Flow

```
User Input → FastAPI → LangChain → Groq AI → Response Parser → JSON → Frontend Display
```



## 🔮 Future Enhancements

- [ ] **Save Ideas**: Allow users to save and export generated ideas
- [ ] **Idea History**: Track previously generated ideas
- [ ] **Advanced Filters**: Add industry, budget, and complexity filters
- [ ] **Multi-language Support**: Generate ideas in different languages
- [ ] **Collaboration Features**: Share ideas with team members
- [ ] **Market Research Integration**: Fetch real-time market data
- [ ] **Business Plan Generator**: Extend ideas into full business plans
- [ ] **User Authentication**: Save user profiles and preferences
- [ ] **API Rate Limiting**: Implement request throttling
- [ ] **Idea Refinement**: Iteratively improve generated ideas

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add comments for complex logic
- Test your changes before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

**Project Link**: [https://github.com/yourusername/IdeaGen-AI](https://github.com/yourusername/IdeaGen-AI)

---

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing ultra-fast AI inference
- [Meta AI](https://ai.meta.com/) for the Llama-3 model
- [LangChain](https://www.langchain.com/) for the LLM framework
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework

---

## ⚠️ Disclaimer

This tool is for educational and brainstorming purposes. Generated ideas should be thoroughly researched and validated before pursuing as a business venture.

---


