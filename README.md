# 🚀 JSO Agent – AI Job Search Optimization Agent

An **Agentic AI system** that helps job seekers generate optimized job search queries and discover opportunities across multiple job platforms.

This project was developed as part of the **JSO Agentic Career Intelligence assignment** to demonstrate how AI agents can improve job discovery workflows.

---

# 📌 Overview

Many job seekers struggle to create effective search queries when using job platforms like LinkedIn, Naukri, or Indeed.

The **AI Job Search Optimization Agent** solves this problem by:

- Understanding user job search intent
- Extracting relevant skills
- Generating optimized job search queries
- Recommending the best job platforms

This system demonstrates how **Agentic AI workflows** can enhance job search efficiency.

---

# 🧠 Key Features

✔ AI-powered job search optimization  
✔ Natural language job search input  
✔ Skill extraction from job query  
✔ Optimized Boolean job search queries  
✔ Job platform recommendations  
✔ Modern interactive frontend UI  
✔ FastAPI backend architecture  
✔ Groq LLM integration  
✔ Docker deployment ready  

---

# 🏗 System Architecture

```
User Interface (Web App)
│
▼
Frontend Layer
HTML / CSS / JavaScript
│
▼
FastAPI Backend API
│
▼
AI Job Search Optimization Agent
│
▼
LLM (Groq - llama-3.3-70b-versatile)
│
▼
Query Generation & Analysis
│
▼
Job Platforms
LinkedIn | Indeed | Naukri | Glassdoor
```

---

# ⚙️ Tech Stack

## Backend
- FastAPI
- Python
- Groq LLM API
- Pydantic
- Python-dotenv

## Frontend
- HTML
- CSS
- JavaScript

## AI
- Groq LLM
- Prompt Engineering
- Structured JSON Output

## Deployment
- Docker
- Render

---

# 📂 Project Structure

```
jso-agent
│
├── app
│   ├── main.py
│   │
│   ├── api
│   │   └── routes.py
│   │
│   ├── agents
│   │   ├── job_agent.py
│   │   └── workflow.py
│   │
│   ├── services
│   │   ├── query_generator.py
│   │   └── prompt_templates.py
│   │
│   └── static
│       ├── index.html
│       ├── style.css
│       └── script.js
│
├── docker
│   └── Dockerfile
│
├── requirements.txt
├── .dockerignore
├── .env
└── README.md
```

---

# 🧪 Example Workflow

User Input:

```
AI Engineer jobs in Bangalore
```

AI Output:

### User Intent
Looking for AI engineering opportunities in Bangalore.

### Skills Detected
Python, Machine Learning, Artificial Intelligence

### Recommended Search Queries
- AI Engineer Bangalore
- Machine Learning Engineer Bangalore
- Artificial Intelligence Developer Bangalore

### Best Platforms
- LinkedIn
- Naukri
- Indeed
- Glassdoor

---

# 🚀 Running the Project Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/jso-agent.git

cd jso-agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Set Environment Variables

Create `.env`

```
GROQ_API_KEY=your_api_key_here
```

---

## 5️⃣ Run the Backend

```bash
uvicorn app.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 🐳 Running with Docker

Build the image:

```bash
docker build -t jso-agent .
```

Run container:

```bash
docker run -p 8000:8000 jso-agent
```

Open:

```
http://localhost:8000
```

---

# 🌐 Deployment

This project can be deployed easily on:

- Render
- Vercel
- AWS
- Google Cloud

Example deployment:

```
Render Docker Web Service
```

---

# 📈 Future Improvements

Planned upgrades:

- Real job fetching from APIs
- Job ranking AI
- Resume matching
- Chat-style job assistant
- Multi-agent workflow

---

# 🤖 AI Agent Design

The system follows an **Agentic AI architecture**:

```
User Query
↓
Intent Analysis Agent
↓
Skill Extraction
↓
Query Generation
↓
Platform Recommendation
```

---

# 📜 License

This project is for **educational and demonstration purposes** as part of the **JSO Agentic AI assignment**.

---

# 👨‍💻 Author

Developed by:

**Yatiraj Kulkarni**

AI / Generative AI Developer

---

# ⭐ Acknowledgement

This project was built as part of the **JSO Phase-2: Agentic Career Intelligence Development Program**.
