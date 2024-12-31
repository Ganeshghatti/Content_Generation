import os
from dotenv import load_dotenv
from crewai import Crew, Process
from .agents import trend_finder, content_writer, creative_writer
from .tasks import trend_task,content_task,creative_task
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

def generate_tweets(keywords):
    keyword = random.choice(keywords)
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
    # print(keyword)
    result = crew1.kickoff(inputs={"niche":keyword})
    result_raw = result.raw
    topics = result_raw.strip().split("\n")
    cleaned_topics = [topic.split(", ", 1)[1] if "," in topic else topic for topic in topics]
    
    result2 = crew2.kickoff(inputs={"topic": cleaned_topics[0]})
    # print(result2)
    return result2

def write_content(prompt):
    crew3 = Crew(
        agents=[creative_writer],
        tasks=[creative_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    result3=crew3.kickoff(inputs={"prompt":prompt})
    print(result3)
    return result3
    
def user_input(keywords,prompt):
    if prompt=="":
        print("No prompt provided, creating content based on keywords")
        return(generate_tweets(keywords=keywords))
    else:
        print("Prompt provided, creating content based on prompt")
        return(write_content(prompt=prompt))

# generate_tweets(["DL","ML","Data Science"])
# write_content("SEO under 200 words")

# print(user_input(["AI","DL"],''))