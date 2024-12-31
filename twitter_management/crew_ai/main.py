import os
from dotenv import load_dotenv
from crewai import Crew, Process
from .agents import create_trend_finder_agent, create_content_writer_agent
from .tasks import trend_task,content_task
import random
# Load environment variables
load_dotenv()

# crew = Crew(
#     agents=[researcher],
#     tasks=[trend_task],
#     process=Process.sequential,
#     memory=True,
#     cache=False,
#     max_rpm=100,
#     share_crew=True,
# )

def generate_tweets(description, keywords, prompt):
    # Create agents with the prompt
    trend_finder = create_trend_finder_agent(prompt)
    content_writer = create_content_writer_agent(prompt)
    
    # Create crews with the new agents
    crew1 = Crew(
        agents=[trend_finder],
        tasks=[trend_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    
    crew2 = Crew(
        agents=[content_writer],
        tasks=[content_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    
    result2 = []
    print(keywords)
    print(description)
    selected_keyword = random.choice(keywords)
    result = crew1.kickoff(inputs={"niche": selected_keyword})
    result_raw = result.raw
    topics = result_raw.strip().split("\n")
    cleaned_topics = [topic.split(", ", 1)[1] if ", " in topic else topic for topic in topics]
    
    result2 = crew2.kickoff(inputs={"topic": cleaned_topics[0], "prompt": prompt})
    print(result2)
    return result2