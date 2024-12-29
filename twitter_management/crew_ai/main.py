import os
from dotenv import load_dotenv
from crewai import Crew, Process
from .agents import researcher
from .tasks import trend_task
# Load environment variables
load_dotenv()

crew = Crew(
    agents=[researcher],
    tasks=[trend_task],
    process=Process.sequential,
    memory=True,
    cache=False,
    max_rpm=100,
    share_crew=True,
)

def generate_tweets(keyword):
    print(keyword)
    result=crew.kickoff(inputs={"niche":keyword})
    return result
