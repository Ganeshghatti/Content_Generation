import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import trend_finder, content_writer
from tasks import trend_task,content_task
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

def generate_tweets(keyword):
    result2=[]
    print(keyword)
    result=crew1.kickoff(inputs={"niche":keyword})
    result_raw=result.raw
    topics = result_raw.strip().split("\n")
    cleaned_topics = [topic.split(", ", 1)[1] if ", " in topic else topic for topic in topics]
    print(cleaned_topics)
    # for topic in cleaned_topics:
    #     print(topic)
    # # result2 = crew2.kickoff(inputs={"topic": topic})
    #     output=crew2.kickoff(inputs={"topic":topic})
    #     result2.append(output)
    #     result2.append("\n")
    #     print(result2)
    result2=crew2.kickoff(inputs={"topic":cleaned_topics[0]})
    print(result2)
    return result2

generate_tweets("Search Engine Optimization")