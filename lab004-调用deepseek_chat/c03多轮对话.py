import os
from openai import OpenAI
import dotenv
dotenv.load_dotenv()
# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("BASE_URL"))

messages = []

while True:
    content = input('User: ')
    messages.append({'role':'user','content':content})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        max_tokens=32,
        temperature=0.7,
        stream=False
    )

    asst_content = response.choices[0].message.content
    messages.append({'role':'assistant','content':asst_content})
    print('Assistant: ',asst_content)


