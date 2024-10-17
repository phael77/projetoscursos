import os
from langchain_openai import ChatOpenAI
from search_tools import SearchTools
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process

load_dotenv()

serper_api_key = os.getenv("SERPER_API_KEY")

if not serper_api_key:
    raise ValueError("SERPER_API_KEY is not set in the environment variables.")