from crewai import Task
from tools import search_tool
from agents import trend_finder, content_writer, creative_writer

# Trend finder task
# trend_task = Task(
#     agent=researcher,
#     description="Research and analyze the latest trends in the {niche} niche",
#     expected_output="A detailed list of the top 3 most trending topics in AI technology, including brief descriptions and their significance",
#     tools=[trend_finder]
# )

trend_task=Task(
    agent=trend_finder,
    description=("Identify the trending topics in {niche} niche."),
    expected_output="A List of top 3 most trending topics based on the {niche} niche",
    tools=[search_tool],
)

# Content writer task
content_task=Task(
    agent=content_writer,
    description=("Write an educating and exciting summary on the topic of {topic}"),
    expected_output="A comprehensive paragraph detailing the information about the topic of {topic}",
    # tools=[search_tool],
    # output_file='content.md'
)

creative_task=Task(
    agent=creative_writer,
    description=("Write an exciting and well informed piece of content based on the following instruction {content}"),
    expected_output="A detailed piece of creative content comprising all the information based on the requirements",
    # tools=[search_tool],
    # output_file='content.md'
)