# openai_integration.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def get_openai_response(messages_for_api):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=messages_for_api,
    )
    return response.choices[0].message['content']
