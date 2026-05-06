from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.baidusearch import BaiduSearchTools
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from dotenv import load_dotenv

db = SqliteDb(db_file="agno.db")
db.clear_memories()

load_dotenv()

def build_agent():
    return Agent(
        db = db,
        model=Groq(id="qwen/qwen3-32b"),
       
        markdown=True,
        add_datetime_to_context=True,
        add_history_to_context=True,
        enable_user_memories= True
    )

agent = build_agent()

user_id = "sameer@gmail.com"

agent.print_response("I am Sameer Sahu and I'm AI/ML Engineer.",  user_id = user_id)
agent.print_response("Who am I?", user_id = user_id)