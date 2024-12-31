from crewai import Agent,LLM
from tools import search_tool
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
llm=LLM(model="groq/gemma2-9b-it", temperature=0.7, max_tokens=1500, api_key=api_key)

# Add tools to agent
trend_finder=Agent(
    role="Trend Analyzer in the niche",
    goal="""Identify and compile a list of current trending topics and searches
				within specific {niche} niche. This list should provide me with the names of the top searches, just the name""",
    description="This agent uses Google Search to find the most trendy topics under a specific niche",
    verbose=True,
    memory=True,
    backstory=(
        """	As a Trending Topic Researcher at a cutting-edge digital
				marketing agency, your primary responsibility is to monitor and
				decode the pulse of the market. Using advanced analytical tools,
				you uncover and list the most relevant trends that can influence
				strategic decisions in content creation."""
    ),
    tools=[search_tool,],
    allow_delegation=True,
    max_retry_limit=2,
    llm=llm
)

content_writer=Agent(
    role="Write Compelling Content on {topic} topic",
    goal=""" Conduct in-depth research on the {topic} topic and compile
				detailed, useful information and insights for each topic. This
				information should be actionable and suitable for creating engaging
				and informed social media posts.""",
    description="This agent uses topics to write an attractive post for content",
    verbose=True,
    memory=True,
    backstory=(
        """As a Content Researcher at a dynamic social media marketing agency,
				you delve deeply into trending topics to uncover underlying themes and
				insights. Your ability to discern and utilize authoritative and relevant
				sources ensures the content you help create resonates with audiences and
				drives engagement."""),
    # tools=[search_tool,],
    allow_delegation=True,
    max_retry_limit=2,
    llm=llm
)