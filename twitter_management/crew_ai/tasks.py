from crewai import Task
from tools import search_tool
from agents import trend_finder, premium_content_writer, premium_creative_writer, basic_content_writer, basic_creative_writer

trend_task=Task(
    agent=trend_finder,
    description=("Identify the trending topics in {niche} niche."),
    expected_output="A List of top 3 most trending topics based on the {niche} niche",
    tools=[search_tool],
)

# Content writer task
premium_content_task=Task(
    agent=premium_content_writer,
    description=("Write an educating and exciting article on the topic of {topic}"),
    expected_output="A comprehensive paragraph in about 500 words detailing the information about the topic of {topic}",
)

premium_creative_task=Task(
    agent=premium_creative_writer,
    description=("Write an exciting and well informed piece of content based on the following instruction {prompt}"),
    expected_output="A detailed piece of creative content comprising all the information based on the requirements",
)

basic_creative_task=Task(
    agent=basic_creative_writer,
    description=("Write an exciting and well informed piece of content strictly under 200 words, based on the following instruction {prompt}"),
    expected_output="A detailed piece of creative content comprising all the information based on the requirements under 200 words",
)

basic_content_task=Task(
    agent=basic_content_writer,
    description=("Write an educating and exciting summary on the topic of {topic}"),
    expected_output="A small paragraph in about 200 words about the topic of {topic}",
)