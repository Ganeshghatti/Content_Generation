from crewai import Task
from .tools import search_tool
from .agents import create_trend_finder_agent, create_content_writer_agent

# Trend finder task
# trend_task = Task(
#     agent=researcher,
#     description="Research and analyze the latest trends in the {niche} niche",
#     expected_output="A detailed list of the top 3 most trending topics in AI technology, including brief descriptions and their significance",
#     tools=[trend_finder]
# )

trend_task=Task(
    agent=create_trend_finder_agent("your_prompt_here"),
    description=("Identify the trending topics in {niche} niche."),
    expected_output="A List of top 3 most trending topics based on the {niche} niche",
    tools=[search_tool],
)

# Content writer task
content_task=Task(
    agent=create_content_writer_agent("your_prompt_here"),
    description=("Write an educating and exciting summary on the topic of {topic}"),
    expected_output="A comprehensive paragraph detailing the information about the topic of {topic}",
    # tools=[search_tool],
    # output_file='content.md'
)