import os

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
import dotenv
dotenv.load_dotenv()


model = ChatOpenAI(
    model=os.getenv('MODEL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('BASE_URL'),
    max_tokens = 128,
)


response = model.invoke([HumanMessage("写一首描述秋天的诗")])
print(response.content)