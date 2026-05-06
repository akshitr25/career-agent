from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import get_response

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "AI Career Planner Running"
    }

@app.get("/ask")
def ask(q: str):

    response = get_response(q)

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)