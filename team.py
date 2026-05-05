from agno.team import Team
from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

eng_agent = Agent(name="English Agent", role="You answer questions in English")
chinese_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hindi_agent = Agent(name="Hindi", role="You answer questions in Hindi")

print(type(eng_agent))
print(type(chinese_agent))
print(type(hindi_agent))

team_leader = Team(
    name = "Answer and Translation Team.",
    members=[eng_agent, chinese_agent,  hindi_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions="""Give response in all three languages. Do not response only in one language.
                        and provide answer of each language in different sections."""
)

team_leader.print_response("What is the capital of India?")
