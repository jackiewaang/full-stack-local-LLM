from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class GenerateRequest(BaseModel):
    model: str
    prompt: str
    stream: bool

@app.post("/")
def generate(req: GenerateRequest):
    r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": req.model,
                "prompt": req.prompt,
                "stream": req.stream
            }
    )

    return r.json()
    
