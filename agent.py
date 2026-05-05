from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.baidusearch import BaiduSearchTools

from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), BaiduSearchTools()],
        markdown=True,
        instructions = "You are a AI/ML Engineer and expert in your.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response("How to become good AI Engineer??")