from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic import hub as prompts
import dotenv
import os
dotenv.load_dotenv()


model = ChatOpenAI(
    model=os.getenv('MODEL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('BASE_URL'),
    max_tokens = 128,
)

prompt = ChatPromptTemplate.from_template("写一首描述{sense}的诗")
chain = prompt | model
url = prompts.push("春天",chain)
print(url)


