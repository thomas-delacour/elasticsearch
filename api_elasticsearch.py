from fastapi import FastAPI
import uvicorn
from elasticsearch import Elasticsearch

api = FastAPI(
    title="API Elasticsearch",
    description="""This API allow to access an Elasticsearch database
    """,
    version="1.0.0",
)

# Connect to Elasticsearch
client = Elasticsearch("http://localhost:9200")


@api.get("/", name="Check API")
def index() -> dict:
    """
    Return a dictionnary that indicate the api is running
    """

    return {"status": "running"}


@api.get("/info", name="Get index informations")
def get_info() -> dict:
    """
    Return informations on indexes in database
    """

    return {"indexes": client.indices.get(index="*")}


if __name__ == "__main__":
    uvicorn.run(
        "api_elasticsearch:api",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
