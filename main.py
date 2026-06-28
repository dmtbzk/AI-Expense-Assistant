from fastapi import FastAPI
from app.api.schemas import ChatRequest, ChatResponse
from app.agent.orchestrator import run
from app.database.connection import create_expense_table



app = FastAPI()
create_expense_table()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat" , response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = run(request.message)
    return ChatResponse(message=answer)