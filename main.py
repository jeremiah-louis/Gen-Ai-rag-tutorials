# import os

# from llama_index.llms.openai import OpenAI

# response = OpenAI(
#     model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY")
# ).complete("who is Mahathma Gandhi?")

# print(response.text)

# print(os.getenv("OPENAI_API_KEY"))
import os

from openai import OpenAI
from dotenv import load_dotenv
from llama_index.core import Settings

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("Enter your prompt here: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    stream=True,
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant. Give detailed and academic explanation in which ever response you create",
        },
        {"role": "user", "content": user_prompt},
    ],
)


for chunk in response:
    print(chunk.choices[0].delta.content, end="")
