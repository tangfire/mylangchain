from langchain_openai import ChatOpenAI
import dotenv
import os
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "写一首描述{sence}的诗,格式要求为{type}")
])

# 格式化
formatted = prompt.format(sence="春天",type="五言律诗")


model = ChatOpenAI(
    model=os.getenv('MODEL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('BASE_URL'),
    max_tokens = 128,
)

resp = model.invoke(formatted)
print(resp.content)


