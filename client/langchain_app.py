import asyncio
import json
from typing import Tuple, List

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

with open('mcp_servers_config.json', 'r') as file:
    mcp_servers_config = json.load(file)


class AgentInput(BaseModel):
    messages: List[Tuple[str, str]]


async def main():
    client = MultiServerMCPClient(mcp_servers_config)
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)

    messages = [("user", "서울 날씨 어때?")]
    print("User: 서울 날씨 어때?")
    response = await agent.ainvoke(AgentInput(messages=messages))  # response.txt 참고
    print("Answer: " + response.get("messages")[-1].content)

    messages = [("user", "50 x 20의 결과는?")]
    print("User: 50 x 20의 결과는?")
    response = await agent.ainvoke(AgentInput(messages=messages))
    print("Answer: " + response.get("messages")[-1].content)


if __name__ == "__main__":
    asyncio.run(main())
