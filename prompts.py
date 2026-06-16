PLANNER_PROMPT = """
You are a strict research planner.

Your task:
Break the user query into 4–6 highly specific subtopics.

Rules:
- Every subtopic MUST be directly related to the query
- Do NOT add generic or unrelated topics
- Keep focus tight and domain-specific
- Return ONLY a Python list

User Query: {query}
"""


RESEARCH_PROMPT = """
You are a research assistant.

Write 5–7 bullet points on:

Topic: {topic}
"""


SUMMARIZE_PROMPT = """
Convert these notes into a clean structured explanation.

Topic: {topic}
Notes: {notes}
"""


REPORT_PROMPT = """
You are a report generator.

Create a structured Markdown report.

Include:
- Title
- Introduction
- Sections (from given data)
- Conclusion

Data:
{sections}
"""