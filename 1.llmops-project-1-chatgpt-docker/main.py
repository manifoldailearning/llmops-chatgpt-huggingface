from fastapi import FastAPI 
from openai import OpenAI
import config
from pydantic import BaseModel
import uvicorn
import time

assistant_id = config.assistant_id
# An empty string would override the SDK's own env lookup, so pass None instead.
api_key = config.api_key or None

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

    # Stop on failure as well as success. The old loop never exited when a run failed.
    terminal_states = {"completed", "failed", "cancelled", "expired", "incomplete"}
    while run.status not in terminal_states:
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(run_id=run.id, thread_id=thread.id)

    if run.status != "completed":
        detail = run.last_error.message if run.last_error else None
        return {"error": run.status, "detail": detail}

    messages = client.beta.threads.messages.list(thread_id=thread.id)
    text = messages.data[0].content[0].text.value
    return {"response": text}   

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)