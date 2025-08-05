from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/")
def generate(model: str, prompt: str, stream: bool):
    r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": stream
            }
    )

    return r.text
    
