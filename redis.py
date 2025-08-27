import asyncio
from toolbox_core.client import ToolboxClient

async def fetch_user_from_redis(email: str):
    try:
        async with ToolboxClient("http://localhost:5000") as client:
            print("Loading tool: get_user_from_redis")
            tool = await client.load_tool("get_user_from_redis")
            print("Executing tool with email:", email)
            result = await tool(email=email)
            return result
    except Exception as e:
        print(f"Error fetching user from Redis: {e}")
        return None
if __name__ == "__main__":
    email = "ajay@example.com"
    result = asyncio.run(fetch_user_from_redis(email))
    if result:
        print("User profile from Redis:", result)
    else:
        print("No user profile found or an error occurred.")