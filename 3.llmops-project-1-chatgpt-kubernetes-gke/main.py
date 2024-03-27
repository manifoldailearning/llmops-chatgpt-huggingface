#!/bin/python3
from fastapi import FastAPI 
from openai import OpenAI
import config
from pydantic import BaseModel
import uvicorn
import os 

assistant_id = config.assistant_id
api_key = os.environ['OPENAI_API']

client = OpenAI(api_key=api_key)

app = FastAPI()

class Body(BaseModel):
    text: str

# get, post, put, and delete

@app.get("/") 
def welcome():
    return {"message": "Welcome to ChatGPT AI Application"}

@app.get("/home") 
def welcome():
    return {"message": "welcome home"}

@app.post("/dummy") 
def demo_function(data):
    return {"message": data}

@app.post("/response")
def generate(body: Body):
    prompt = body.text # user input
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id=assistant_id
    )

    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            break;
    return text   

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)