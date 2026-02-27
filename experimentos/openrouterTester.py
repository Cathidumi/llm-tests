import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI


def tester():
    # Test the OpenRouter API
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key= OPENROUTER_API_KEY,
    )

    completion = client.chat.completions.create(
      model="openai/gpt-5.2",
      messages=[
        {
          "role": "user",
          "content": "What is the meaning of life in one word?"
        }
      ]
    )

    print(completion.choices[0].message.content)

def get_limits():
    # Get the usage limits for the API key
    load_dotenv()
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    response = requests.get(
    url="https://openrouter.ai/api/v1/key",
    headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}"
        }
    )
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    #tester()
    print()
    get_limits()

