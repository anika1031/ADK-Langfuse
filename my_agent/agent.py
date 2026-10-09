from dotenv import load_dotenv
load_dotenv()

from langfuse import get_client
from openinference.instrumentation.google_adk import GoogleADKInstrumentor

langfuse = get_client()
if langfuse.auth_check():
    print("Langfuse connected")
else:
    print("Langfuse auth failed - check keys and host")

GoogleADKInstrumentor().instrument()

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def get_word_count(text: str) -> dict:
    """Counts the words in the given text."""
    return {"word_count": len(text.split())}

root_agent = Agent(
    name="groq_agent",
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    instruction="You are a helpful assistant. Use tools when they are useful.",
    tools=[get_word_count],
)

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def get_word_count(text: str) -> dict:
    """Counts the words in the given text."""
    return {"word_count": len(text.split())}

root_agent = Agent(
    name="groq_agent",
    model=LiteLlm(model="groq/openai/gpt-oss-20b"),
    instruction="You are a helpful assistant. Use tools when they are useful.",
    tools=[get_word_count],
)
root_agent = Agent(
    name="groq_agent",
    model=LiteLlm(
        model="groq/openai/gpt-oss-20b",
        include_reasoning=False,
    ),
    instruction="You are a helpful assistant. Use tools when they are useful.",
    tools=[get_word_count],
)