import asyncio
from toolbox_core import ToolboxClient

async def main():
    async with ToolboxClient("http://localhost:5000") as client:
        try:
            ref_tool = await client.load_tool("get_product_by_ref")
            barcode_tool = await client.load_tool("get_product_by_barcode")
            print(" Supabase tools loaded successfully")
            print(" Searching by ref...")
            ref_results = await ref_tool() 
            print(f"Results by ref: {ref_results}")
            print("Searching by barcode...")
            barcode_results = await barcode_tool()  
            print(f"Results by barcode: {barcode_results}")
        except Exception as e:
            print(" Error:", str(e))
if __name__ == "__main__":
    asyncio.run(main())