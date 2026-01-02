import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("BASE_URL"))


# response = client.embeddings.create(
#     model=os.getenv("MODEL_EMBEDDING"),
#     input="感冒了吃什么药好得快？"
# )

# print(response)
# print(len(response.data[0].embedding))

response = client.embeddings.create(
    model=os.getenv("MODEL_EMBEDDING"),
    input=["感冒了吃什么药好得快？", "阿莫西林能治感冒吗？"]
)

for item in response.data:
    print(len(item.embedding))

