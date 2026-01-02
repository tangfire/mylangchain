# 流式stream
import os
from openai import OpenAI
import dotenv
dotenv.load_dotenv()
# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("BASE_URL"))

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "最近有什么大事发生嘛？"},
  ],
    max_tokens=32,
    temperature=0.7,
    stream=True
)

for chunk in response:
    if len(chunk.choices) > 0:
        content = chunk.choices[0].delta.content
        print(content,end="")
