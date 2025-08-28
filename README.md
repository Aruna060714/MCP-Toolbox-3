## MongoDB & Supabase Toolbox
This project demonstrates how to build a MongoDB, Supabase, OpenSearch,Redis and MySQL-backed tool system using the Toolbox framework. It allows you to query MongoDB databases, Supabase REST API, OpenSearch, and MySQL through a Toolbox server, with tools defined in a YAML configuration file (tools.yaml).
## Project Structure
    .
    ├── toolbox.py            # Client script that connects to Toolbox server for MongoDB queries
    ├── supabase.py           # Client script that connects to Toolbox server for Supabase queries
    ├── opensearch.py         # Client script that connects to Toolbox server for OpenSearch queries
    ├── redis.py              # Client script that connects to Toolbox server for Redis queries
    ├── mysql.py              # Client script that connects to Toolbox server for MySQL product queries
    ├── api_opensearch.py     # FastAPI server for OpenSearch product search
    ├── tools.yaml            # Toolbox configuration (sources + tools for MongoDB, Supabase, OpenSearch, MySQL)
    ├── docker-compose.yaml   # Docker config to run MongoDB, MySQL, and Toolbox server
    └── .env                  # Environment variables (create from .env.example)
## Data Sources
- **MongoDB**: Stores user data (email, name, etc.)
- **Supabase**: Stores product data with REST API endpoints
- **OpenSearch**: Provides search capabilities for product data via FastAPI
- **MySQL**: Stores product details, allows fetching products by type
- **redis** : connects to Toolbox server for Redis queries 

## Available Tools
1. **get_user_profile**: Query MongoDB for user profiles by email address
2. **get_product_by_ref**: Fetch product details from Supabase by product reference
3. **get_product_by_barcode**: Fetch product details from Supabase by barcode
4. **search_products**: Search products in OpenSearch by title, category, or description
5. **get_products_by_type**: Query MySQL to fetch products by their type
6. **get_user_from_redis** : Fetch user profile from Redis by email

## Workflow Overview
1. MongoDB stores user data, Supabase stores product data
2. tools.yaml defines tools to query both data sources
3. Toolbox Server (runs on http://localhost:5000) exposes these tools as an API
4. toolbox.py → connects to Toolbox server for MongoDB queries
5. supabase.py → connects to Toolbox server for Supabase product queries
6. opensearch.py → connects to Toolbox server for OpenSearch product searches
7. api_opensearch.py → FastAPI server that interfaces with OpenSearch
8. mysql.py → connects to Toolbox server for MySQL product queries
9. redis.py → stores user profiles.

## Environment Variables (.env file)
Create a `.env` file in the project root with the following variables:

```env
# MongoDB Connection
MONGODB_URI=<YOUR MONGODB_URI>

# Supabase Configuration
SUPABASE_URL=<YOUR SUPABASE_URL>
SUPABASE_API_KEY=<your-supabase-anon-key>

# OpenSearch Configuration
OPENSEARCH_HOST=<your-opensearch-host>
OPENSEARCH_PORT=443
OPENSEARCH_USER=admin
OPENSEARCH_PASS=admin

# MySQL Configuration
MYSQL_HOST=
MYSQL_PORT=3306
MYSQL_DATABASE=
MYSQL_USER=
MYSQL_PASSWORD=<YOUR_MYSQL_PASSWORD>

#Redis Configuration
REDIS_HOST=
REDIS_PORT=
```
## Setup Instructions
1. **Create & Activate Python Virtual Environment**:
    ```bash
    python -m venv venv
    ```

    To activate:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`

2. **Install Python Dependencies**:
    ```bash
    pip install toolbox-core fastapi uvicorn opensearch-py python-dotenv
    ```

3. **Start Services with Docker**
    ```bash
    docker-compose up -d
    ```

    This will:
    - Start a MongoDB container
    - Start a Toolbox server on http://localhost:5000, using tools.yaml
4. **Start OpenSearch API Server (in a separate terminal)**:

  ```bash
       uvicorn api_opensearch:app --reload --host 0.0.0.0 --port 8000
  ```

5. **Run Toolbox Clients**
    - For MongoDB queries:
      ```bash
      python toolbox.py
      ```
      - Connects to Toolbox server (http://localhost:5000)
      - Loads the get_user_profile tool
      - Calls it with email="john@example.com"
      - Prints the result as JSON

    - For Supabase product queries:
      ```bash
      python supabase.py
      ```
      - Connects to Toolbox server (http://localhost:5000)
      - Loads both product query tools (by ref and by barcode)
      - Executes queries and prints results
    
    - For opensearch product queries:
    ```bash
      python opensearch.py
    ```
      - Connects to Toolbox server (http://localhost:5000)
      - Loads the search_products tool
      - Executes search with predefined query
      - Prints formatted product results
    - For mysql product queries:
    ```bash
    python mysql.py
    ```
      - Connects to Toolbox server (http://localhost:5000)
      - Loads the get_products_by_type tool
      - Calls it with a product type (e.g., "jersey")
      - Prints formatted results
    - For redis user queries:
    ```bash
    python redis.py
    ```
      - Connects to Toolbox server (http://localhost:5000)
      - Loads the get_user_from_redis tool
      - Calls it with an email (e.g., "ajay@example.com")
      - Prints the user profile stored in Redis (as JSON)

## Example Outputs

**MongoDB Query Output**:
```json
{
  "_id": {
    "$oid": "689d9a9d234aacd0c6661a7e"
  },
  "age": 30,
  "email": "john@example.com",
  "name": "John Doe",
  "role": "designer"
}
```
**Supabase Query Output** :
```
  Supabase tools loaded successfully
  Searching by ref...
  Results by ref: [{...product data...}]
  Searching by barcode...
  Results by barcode: [{...product data...}]
```
**OpenSearch Query Output**:
  ```Query result:
  {
    "results": [
      {
        "barcode": "3664142014010",
        "brand": "SWAP",
        "ref": "12041451",
        "title": "TURBINE VENTILATION M"
      }
    ],
    "total": 16
  }

  Product Details:
  Title: TURBINE VENTILATION M
  Ref: 12041451
  Barcode: 3664142014010
  Brand: SWAP
  ----------------------------------------
```
**mysql uqery output**:
  ID: 1
  Title: Opna Women's Short Sleeve Moisture
  Type: jersey
  Image: https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg

**redis output**:
  Loading tool: get_user_from_redis
  Executing tool with email: ajay@example.com
  User profile from Redis: ["{\"email\": \"ajay@example.com\", \"name\": \"Ajay\", \"age\": 30, \"role\": \"designer\"}"]