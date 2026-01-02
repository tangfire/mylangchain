# pip install -qU langchain "langchain[anthropic]"
import os
import dotenv
dotenv.load_dotenv()
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 创建带代理的模型
llm = ChatOpenAI(
    model=os.getenv("MODEL"),
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    # 使用国内代理服务（示例，需替换为实际可用的）
    base_url=os.getenv("BASE_URL"),
)

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
resp = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

print(resp)
print("--------------------")
print(resp["messages"][-1].content)