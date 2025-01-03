from crewai import Agent, LLM
from tools import search_tool
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = LLM(model="groq/gemma2-9b-it", temperature=0.7, max_tokens=1500, api_key=api_key)

trend_finder=Agent(
        role="Trend Analyzer in the {niche} niche",
        goal="""Identify and compile a list of current trending topics and searches
                within specific {niche} niche. This list should provide me with the names of the top searches, just the name""",
        description="This agent uses Google Search to find the most trendy topics under {niche} niche",
        verbose=True,
        memory=True,
        backstory=(
            """As a Trending Topic Researcher specializing in {niche}, your primary responsibility 
               is to monitor and decode the pulse of the market."""
        ),
        tools=[search_tool,],
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
)

premium_content_writer=Agent(
        role="Write Compelling Content for {topic} in no less than 500 words",
        goal="""Conduct in-depth research on the topic and compile detailed information 
                following this topic: {topic}, and write a post in about 500 words""",
        description="This agent uses topics to write an attractive post for content",
        verbose=True,
        memory=True,
        backstory=(
            """As a Content Researcher specializing in {topic}, you create detailed
               and long form social media posts."""
        ),
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
)

premium_creative_writer=Agent(
        role="Write Compelling Content based on the following instruction {prompt}",
        goal="""Conduct in-depth research on the topic and write an article of detailed information on the 
                following: {prompt}""",
        description="This agent uses topics to write an attractive post for content",
        verbose=True,
        memory=True,
        backstory=(
            """As a Senior Creative Writer specializing in various fields, you create engaging
               and informed social media posts."""
        ),
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
)

basic_content_writer=Agent(
        role="Write Compelling Content for {topic} under 200 words",
        goal="""Conduct in-depth research on the topic and compile detailed information 
                following this topic: {topic} under 200 words""",
        description="This agent uses topics to write an attractive post for content",
        verbose=True,
        memory=True,
        backstory=(
            """As a Content Researcher specializing in {topic}, you create engaging
               and short form social media posts."""
        ),
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
)

basic_creative_writer=Agent(
        role="Write Compelling Content under 200 words based on the following instruction {prompt}",
        goal="""Conduct in-depth research on the topic and write an article under 200 words on the 
                following: {prompt}""",
        description="This agent uses topics to write an attractive post for content",
        verbose=True,
        memory=True,
        backstory=(
            """As a Senior Creative Writer specializing in various fields, you create engaging
               and informed social media posts under 200 words"""
        ),
        allow_delegation=True,
        max_retry_limit=2,
        llm=llm
)

