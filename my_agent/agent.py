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

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def get_word_count(text: str) -> dict:
    """Counts the words in the given text."""
    return {"word_count": len(text.split())}

def check_if_palindrome(text: str) -> dict:
    """Checks if the given text is a palindrome."""
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    return {"is_palindrome": cleaned_text == cleaned_text[::-1]}

root_agent = Agent(
    name="groq_agent",
    model=LiteLlm(
        model="groq/openai/gpt-oss-20b",
        include_reasoning=False,
    ),
    instruction="You are a helpful assistant. Use the tools provided to answer questions. " \
    "Use get_word_count to count the number of words in a given text and " \
    "check_if_palindrome to determine if a given text is a palindrome.",
    tools=[get_word_count, check_if_palindrome],
)
