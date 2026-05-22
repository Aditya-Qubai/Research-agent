from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client_ai = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def critique_text(text):

    prompt = f"""
    You are a scientific peer reviewer.

    Critique this research summary:

    {text}
    """

    response = client_ai.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content