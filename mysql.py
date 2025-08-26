import asyncio
import json
from toolbox_core.client import ToolboxClient
async def fetch_products_by_type(product_type: str):
    async with ToolboxClient("http://localhost:5000") as client:
        tool = await client.load_tool("get_products_by_type")
        result = await tool(type=product_type)
        return result
def print_products(products):
    if not products:
        print("No products found.")
        return
    for prod in products:
        print(f"ID: {prod.get('id', 'N/A')}")
        print(f"Title: {prod.get('title', 'N/A')}")
        print(f"Type: {prod.get('type', 'N/A')}")
        print(f"Image: {prod.get('image', 'N/A')}")
        print("-" * 40)
if __name__ == "__main__":
    product_type = "jersey"
    result = asyncio.run(fetch_products_by_type(product_type))
    products = json.loads(result)
    print_products(products)