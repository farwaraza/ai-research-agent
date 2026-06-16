from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

import os
from groq import Groq
from dotenv import load_dotenv
from prompts import *

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ---------------- LLM CALL ---------------- #

def call_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------------- 1. PLANNER (Agentic AI) ---------------- #

def planner(query):
    """
    Agent step 1: Breaks task into subtasks
    """
    prompt = PLANNER_PROMPT.format(query=query)
    result = call_llm(prompt)

    return eval(result)   # expected Python list


# ---------------- 2. TOOL CALLING LAYER ---------------- #

def research_tool(query, topic):
    """
    This simulates TOOL CALLING (IMPORTANT FOR YOUR SPEC)
    """
    prompt = f"""
You are a research tool.

User Query: {query}
Subtask: {topic}

Return only factual bullet points relevant to the query.
"""
    return call_llm(prompt)


# ---------------- 3. SUMMARIZER ---------------- #

def summarize(topic, notes):
    prompt = SUMMARIZE_PROMPT.format(topic=topic, notes=notes)
    return call_llm(prompt)


# ---------------- 4. REPORT GENERATOR ---------------- #

def generate_report(sections):
    prompt = REPORT_PROMPT.format(sections=sections)
    return call_llm(prompt)

def generate_pdf(text):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    # Split report into lines
    for line in text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 8))

    doc.build(content)

    buffer.seek(0)
    return buffer