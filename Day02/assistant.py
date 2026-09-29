from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
    )
messages=[]
while True:
    user_input=input("Enter yr questions : ")

    messages.append({"role":"user","content":user_input})

    response=client.chat.completions.create(model=os.getenv("MODEL"),messages=messages)

    print(response.choices[0].message.content)
    messages.append({"role":"assistant","content":response.choices[0].message.content})

    for message in messages:
        print(f"{message['role']}:{message['content']}\n")

    res=input("Do u wnat to quit ? (Y/N)")
    if res.lower()=='y':
        break


