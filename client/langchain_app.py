import asyncio
import json
from typing import Tuple, List

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel
from langchain.agents import create_react_agent

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

with open('mcp_servers_config.json', 'r') as file:
    mcp_servers_config = json.load(file)


class AgentInput(BaseModel):
    messages: List[Tuple[str, str]]


async def main():
    # MultiServerMCPClient는 mcp_servers_config.json 설정을 읽어 MCP 서버들과 통신
    # MCP 프로토콜로 제공되는 도구들을 LangChain이 즉시 사용할 수 있는 표준 Tool 객체 리스트로 변환
    # 나중에 에이전트가 Tool을 실행하면, 자동으로 MultiServerMCPClient를 통해 올바른 MCP API를 호출
    client = MultiServerMCPClient(mcp_servers_config)
    tools = await client.get_tools()

    # create_react_agent는 ReAct Agent의 동작을 구현한 그래프를 반환
    # 아래 react_agent_graph.invoke() 함수 호출은 그래프의 시작점을 호출하는 것
    react_agent_graph = create_react_agent(model, tools)

    messages = [("user", "서울 날씨 어때?")]
    print("User: 서울 날씨 어때?")
    response = await react_agent_graph.ainvoke(AgentInput(messages=messages))  # response.txt 참고
    print("Answer: " + response.get("messages")[-1].content)

    messages = [("user", "50 x 20의 결과는?")]
    print("User: 50 x 20의 결과는?")
    response = await react_agent_graph.ainvoke(AgentInput(messages=messages))
    print("Answer: " + response.get("messages")[-1].content)


if __name__ == "__main__":
    asyncio.run(main())
