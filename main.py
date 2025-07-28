from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def get_weather(city: str) -> str:
   """ # MCP 클라이언트 측에 표시되는 설명
   도시의 날씨를 반환합니다.

   :param city: The city to get the weather for
   """
   return f"{city} weather is good"

if __name__ == "__main__":
   print("Starting MCP server...")
   mcp.run(transport="stdio")
