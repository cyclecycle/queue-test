from typing import List
from fastapi import FastAPI, BackgroundTasks
from redis import Redis
from rq import Queue
import uuid
from shared.db import init_db
from logging import getLogger
from pydantic import BaseModel

logger = getLogger(__name__)


app = FastAPI()
redis_conn = Redis(host="redis", port=6379)


@app.on_event("startup")
def startup_event():
    init_db()


class SearchRequest(BaseModel):
    queries: List[str]


@app.post("/enqueue")
async def search(request: SearchRequest, background_tasks: BackgroundTasks):
    queries = request.queries
    q = Queue(connection=redis_conn)
    job_id = str(uuid.uuid4())
    for query in queries:
        background_tasks.add_task(enqueue_fetch_document, query)
    return {"message": "Queries enqueued", "count": len(queries)}


def enqueue_fetch_document(query: str):
    q = Queue(connection=Redis(host="redis", port=6379))
    q.enqueue("tasks.fetch_documents", query)
