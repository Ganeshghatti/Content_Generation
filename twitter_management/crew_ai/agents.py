from crewai import Agent, LLM
from .tools import search_tool
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = LLM(model="groq/gemma2-9b-it", temperature=0.7, max_tokens=1500, api_key=api_key)

def create_trend_finder_agent(prompt):
    print(prompt)
    return Agent(
        role=f"Trend Analyzer in the {prompt} niche",
        goal=f"""Identify and compile a list of current trending topics and searches
                within specific {prompt} niche. This list should provide me with the names of the top searches, just the name""",
        description=f"This agent uses Google Search to find the most trendy topics under {prompt} niche",
        verbose=True,
        memory=True,
        backstory=(
            f"""As a Trending Topic Researcher specializing in {prompt}, your primary responsibility 
               is to monitor and decode the pulse of the market."""
        ),
        tools=[search_tool,],
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
    )

def create_content_writer_agent(prompt):
    return Agent(
        role=f"Write Compelling Content for {prompt}",
        goal=f"""Conduct in-depth research on the topic and compile detailed information 
                following this prompt: {prompt}""",
        description="This agent uses topics to write an attractive post for content",
        verbose=True,
        memory=True,
        backstory=(
            f"""As a Content Researcher specializing in {prompt}, you create engaging
               and informed social media posts."""
        ),
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
    )