from pprint import pprint

# OpenAI API 키 환경설정 변수로 설정하기 
# echo 'export OPENAI_API_KEY="API_KEY"' >> ~/.bashrc
# source ~/.bashrc

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


model = "gpt-4o-mini-2024-07-18"

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]

response = client.chat.completions.create(model=model, messages=messages).model_dump()
pprint(response)