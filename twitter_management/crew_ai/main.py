import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import trend_finder, premium_content_writer, basic_creative_writer, basic_content_writer, premium_creative_writer
from tasks import trend_task,premium_content_task,basic_creative_task,basic_content_task, premium_creative_task
import random
# Load environment variables
load_dotenv()

def premium_generation(keywords):
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
        agents=[premium_content_writer],
        tasks=[premium_content_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    
    result2 = []
    print(keyword)
    result = crew1.kickoff(inputs={"niche":keyword})
    result_raw = result.raw
    topics = result_raw.strip().split("\n")
    cleaned_topics = [topic.split(", ", 1)[1] if "," in topic else topic for topic in topics]
    
    result2 = crew2.kickoff(inputs={"topic": cleaned_topics[0]})
    # print(result2,"\n")
    return result2

def premium_content(prompt):
    crew3 = Crew(
        agents=[premium_creative_writer],
        tasks=[premium_creative_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    result3=crew3.kickoff(inputs={"prompt":prompt})
    print(result3,"\n")
    return result3
    
def basic_generation(keywords):
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
        agents=[basic_content_writer],
        tasks=[basic_content_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    
    result2 = []
    print(keyword)
    result = crew1.kickoff(inputs={"niche":keyword})
    result_raw = result.raw
    topics = result_raw.strip().split("\n")
    cleaned_topics = [topic.split(", ", 1)[1] if "," in topic else topic for topic in topics]
    
    result2 = crew2.kickoff(inputs={"topic": cleaned_topics[0]})
    # print(result2,"\n")
    return result2

def basic_content(prompt):
    crew3 = Crew(
        agents=[basic_creative_writer],
        tasks=[basic_creative_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )
    result3=crew3.kickoff(inputs={"prompt":prompt})
    print(result3,"\n")
    return result3



def premium_user(description,keywords, prompt,prem_token):
    if prem_token:
        if prompt==None:
            print("No prompt provided, creating content based on keywords")
            return(premium_generation(keywords=keywords))
        else:
            print("Prompt provided, creating content based on prompt")
            return(premium_content(prompt=prompt))
    else:
        return basic_user(description,keywords,prompt)


def basic_user(description,keywords, prompt):
    if prompt==None:
        print("No prompt provided, creating content based on keywords")
        return(basic_generation(keywords=keywords))
    else:
        print("Prompt provided, creating content based on prompt")
        return(basic_content(prompt=prompt))

# generate_tweets(["DL","ML","Data Science"])
# write_content("SEO under 200 words")

print(premium_user("desc",["AI","DL","SEO","Banana"],"Banana Recipe",False))