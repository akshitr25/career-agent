from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from prompts import SYSTEM_PROMPT,CRITIQUE_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_response(user_input):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    roadmap = response.choices[0].message.content

    critique_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": CRITIQUE_PROMPT
            },
            {
                "role": "user",
                "content": roadmap
            }
        ]
    )

    critique = critique_response.choices[0].message.content

    roadmap_json = json.loads(roadmap)

    return {
        **roadmap_json,
        "critique": critique
    }