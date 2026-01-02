import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": ["/path/to/math_server.py"],
            },
            "weather": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",
            }
        }
    )

    llm = ChatOpenAI(
        model=os.getenv("MODEL"),
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )

    tools = await client.get_tools()
    agent = create_agent(
        model=llm,
        tools=tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    print("Math Response:", math_response)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print("Weather Response:", weather_response)


# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(main())