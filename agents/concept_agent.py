from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client_ai = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def extract_concepts(text):

    prompt = f"""
    Extract key scientific concepts from this:

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