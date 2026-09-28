from openai import OpenAI
from dotenv import load_dotenv

import os

#load configuration
load_dotenv()

#create AI client

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="  * 40)
print("      My AI Assistant")
print("="  * 40)

messages=[]
while True:

    prompt = input("Enter your prompt:   ")
    response=client.chat.completions.create( model=os.getenv("MODEL"),messages=[
    {
     "role":"user",
     "content":prompt
    }
    ])
    print(response.choices[0].message.content)

    print("Do you want to continue? (y/n)")
    choice =input()
    if(choice.lower()=='n'):
        break





