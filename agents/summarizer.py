from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client_ai = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def summarize_text(text):

    prompt = f"""
    Summarize this research paper:

    {text[:2000]}
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