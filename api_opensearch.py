from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from opensearchpy import OpenSearch
import os
from dotenv import load_dotenv
load_dotenv()
HOST = os.getenv("OPENSEARCH_HOST", "localhost")
PORT = int(os.getenv("OPENSEARCH_PORT", 443))
USER = os.getenv("OPENSEARCH_USER", "admin")
PASS = os.getenv("OPENSEARCH_PASS", "admin")
client = OpenSearch(
    hosts=[{"host": HOST, "port": PORT}],
    http_auth=(USER, PASS),
    use_ssl=True,
    verify_certs=False,
)
app = FastAPI(title="OpenSearch Products API")
class SearchRequest(BaseModel):
    query: str
    size: int = 10  
@app.post("/search")
def search_products(req: SearchRequest):
    index_name = "products_new"  
    search_query = {
        "query": {
            "multi_match": {
                "query": req.query,
                "fields": ["title^2", "category", "description"]  
            }
        },
        "_source": ["title", "ref", "barcode", "brand"],  
        "size": req.size
    }
    try:
        response = client.search(index=index_name, body=search_query)
        results = [hit["_source"] for hit in response["hits"]["hits"]]
        return {"total": response["hits"]["total"]["value"], "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))