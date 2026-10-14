import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    server_url = "https://your-recipe-service.onrender.com/mcp"

    async with streamablehttp_client(server_url) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(
            read_stream, write_stream
        ) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", tools.tools)

            result = await session.call_tool(
                "search_recipes",
                {
                    "ingredient": "potato",
                    "vegetarian_only": True,
                },
            )

            print(result.content)


if __name__ == "__main__":
    asyncio.run(main())