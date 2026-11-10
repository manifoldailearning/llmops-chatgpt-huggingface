#!/bin/python3
from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

# GPT-2 runs on PyTorch in current transformers. device=-1 keeps it on CPU.
generator = pipeline("text-generation", model="gpt2", device=-1)
app = FastAPI(
    title="Fast API App for LLM Model",
    description="A Text Generator App",
    version="1.0",
)


class Body(BaseModel):
    text: str


@app.get("/")
def index():
    return HTMLResponse("<h1>Welcome to LLMOps Course with a GPT2 model V1</h1>")


@app.post("/generate")
def predict(body: Body):
    # max_new_tokens limits the completion. max_length counted the prompt too.
    results = generator(body.text, max_new_tokens=60, num_return_sequences=1)
    return {"generated_text": results[0]["generated_text"]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
