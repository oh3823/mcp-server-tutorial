from mcp.server.fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def multiply(a: int, b: int) -> str:
    """
    두 수의 곱을 반환합니다.

    :param a: 곱셈의 첫 번째 피연산자
    :param b: 곱셈의 두 번째 피연산자
    :return: 두 수의 곱셈 결과
    """
    return str(a * b)


if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")
