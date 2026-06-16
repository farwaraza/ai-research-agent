# AI Research Agent (Agentic AI System)

An AI-powered multi-step research assistant that converts user queries into structured, well-organized research reports using an Agentic AI workflow.

---

##  Features

- **Multi-step AI Agent Workflow** (Planning → Research → Summarization → Report Generation)  
- **Agentic AI System** using LLM-based task decomposition  
- Generates structured **Markdown research reports**  
- Real-time execution using **Streamlit UI**  
- **PDF Export** of AI-generated reports  
- Session-based **research history tracking**  
- Powered by **Groq LLaMA 3.3**

---

## System Architecture

User Query → Planner Agent → Research Tool → Summarizer → Report Generator → Final Output

---

## How It Works

### 1. Planner Agent
Breaks the user query into structured subtopics.

### 2. Research Tool
Uses LLM calls to generate topic-wise research notes.

### 3. Summarizer
Converts raw notes into clean, structured insights.

### 4. Report Generator
Combines all sections into a final structured report.

### 5. Streamlit UI
Displays results in real time and allows PDF download.

---

## Tech Stack

- Python  
- Groq API (LLaMA 3.3)  
- Streamlit  
- ReportLab (PDF generation)  
- dotenv  

---

## Project Structure

```
AI-Research-Agent/
│
├── app.py              # Streamlit UI
├── agent.py            # Agent workflow logic
├── prompts.py          # Prompt templates
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-agent.git
cd ai-research-agent
```
### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
```
# Activate environment
```bash
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables 

Create a .env file in the root folder and add:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
You can get your API key from:
https://console.groq.com/

### 5. Run the Streamlit app
```bash
streamlit run app.py
```

---

## Project Highlights
- Built an AI system that breaks a user question into smaller parts and solves them step-by-step
- Used multiple LLM calls in sequence to plan, research, and generate a final report
- Designed a simple “tool-like” workflow where each step has a specific job (planner, researcher, summarizer, report writer)
- Created a working AI research assistant that produces structured reports from a single user input
