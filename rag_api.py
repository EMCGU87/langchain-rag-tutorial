from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# -- Import the rag_query setup from your query notebook/script --
from rag_service import rag_query  # Or copy relevant code from your notebook

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    response: str
    sources: List[str]
    found: bool

@app.post("/query", response_model=QueryResponse)
def query_endpoint(q: QueryRequest):
    result = rag_query(q.question)
    return QueryResponse(**result)

@app.get("/health")
def health():
    return {"ok": True}