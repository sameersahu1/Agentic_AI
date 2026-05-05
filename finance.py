from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.baidusearch import BaiduSearchTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), BaiduSearchTools(), YFinanceTools()],
        markdown=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use the given tools whever needed. Format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context=True, 
        debug_mode = True
    )

agent = build_agent()
agent.print_response("What is current stock  microsoft in INR?")





