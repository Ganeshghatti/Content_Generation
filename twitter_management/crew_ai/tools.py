from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

search_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    # country="In",
    # locale="en",
    # location="Bengaluru, Karnataka, India",
    n_results=2,
)
