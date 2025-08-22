import asyncio
import json
from toolbox_core import ToolboxClient
async def main():
    async with ToolboxClient("http://localhost:5000") as client:
        try:
            tool = await client.load_tool("get_user_profile")
            print(" Tool loaded successfully")
            result_str = await tool(email="john@example.com")
            if not result_str:
                print("No results found")
                return
            try:
                result_data = json.loads(result_str)
                if isinstance(result_data, list):
                    if len(result_data) > 0:
                        result = result_data[0]  
                    else:
                        print("Empty result array")
                        return
                else:
                    result = result_data
                result.pop('password_hash', None)
                result.pop('login_history', None)
                print(" Query result:")
                print(json.dumps(result, indent=2))
            except json.JSONDecodeError:
                print(" Invalid JSON response:")
                print(result_str)
        except Exception as e:
            print("Error:", str(e))
            import traceback
            traceback.print_exc()
if __name__ == "__main__":
    asyncio.run(main())