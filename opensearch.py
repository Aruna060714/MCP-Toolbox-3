import asyncio
import json
from toolbox_core import ToolboxClient
async def test_opensearch():
    async with ToolboxClient("http://localhost:5000") as client:
        try:
            search_tool = await client.load_tool("search_products")
            print("OpenSearch API tool loaded successfully")
            results = await search_tool()
            if not results:
                print("No results found")
                return
            try:
                result_data = json.loads(results)
                print("Query result:")
                print(json.dumps(result_data, indent=2))
                if result_data.get("results"):
                    print("\nProduct Details:")
                    for product in result_data["results"]:
                        print(f"Title: {product.get('title', 'N/A')}")
                        print(f"Ref: {product.get('ref', 'N/A')}")
                        print(f"Barcode: {product.get('barcode', 'N/A')}")
                        print(f"Brand: {product.get('brand', 'N/A')}")
                        print("-" * 40)
                else:
                    print("No products found in response")
            except json.JSONDecodeError:
                print("Invalid JSON response:")
                print(results)
        except Exception as e:
            print("Error:", str(e))
            import traceback
            traceback.print_exc()
if __name__ == "__main__":
    asyncio.run(test_opensearch())