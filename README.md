# AI Career Planner

AI-powered career roadmap generator built using FastAPI, OpenAI API, and dynamic frontend rendering.

Users can enter a career goal such as:

```text
Become AI Engineer
```

and receive:
- phase-wise roadmap
- skills to learn
- project recommendations
- estimated timelines

---

# Live Demo

## Frontend
https://akshitr25.github.io/career-agent/

## Backend API
https://career-agent-0rnw.onrender.com

---

# Features

- AI-generated career roadmaps
- Structured JSON output
- Dynamic frontend rendering
- FastAPI backend
- OpenAI API integration
- GitHub Pages frontend deployment
- Render backend deployment
- Responsive roadmap cards
- CORS-enabled frontend/backend communication

---

# Tech Stack

## Backend
- Python
- FastAPI
- OpenAI API
- Uvicorn

## Frontend
- HTML
- CSS
- JavaScript

## Deployment
- Render
- GitHub Pages

---

# Project Architecture

```text
Frontend (GitHub Pages)
        ↓
FastAPI Backend (Render)
        ↓
OpenAI API
        ↓
Structured JSON Response
        ↓
Dynamic Roadmap Rendering
```

---

# Example API Response

```json
{
  "goal": "Become AI Engineer",
  "phases": [
    {
      "phase_name": "Foundation",
      "skills": [
        "Python",
        "Data Structures"
      ],
      "projects": [
        "Calculator App"
      ],
      "timeline": "0-3 months"
    }
  ]
}
```

---

# Local Setup

## Clone repository

```bash
git clone https://github.com/akshitr25/career-agent.git
cd career-agent
```

---

## Create virtual environment

```bash
python -m venv venv
```

---

## Activate virtual environment

### Windows CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Add environment variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Run application

```bash
python app.py
```

OR

```bash
uvicorn app:app --reload
```

---

# Frontend Setup

Inside `index.html`, use:

```javascript
http://127.0.0.1:8000
```

for local development.

Use deployed Render URL for production.

---

# Future Improvements

- User authentication
- Save roadmap history
- Download roadmap as PDF
- Multi-agent reviewer system
- Personalized recommendations
- Progress tracking
- Database integration

---

# Learning Outcomes

This project demonstrates:

- AI system orchestration
- Structured LLM outputs
- FastAPI backend development
- Frontend/backend integration
- Deployment workflows
- Dynamic UI rendering
- API design
- JSON-driven applications

---

# Author

Akshit Rathod

GitHub:
https://github.com/akshitr25