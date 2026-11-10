from fastapi import FastAPI 
from openai import OpenAI
import config
from pydantic import BaseModel
import uvicorn

vector_store_id = config.vector_store_id
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
    # The Assistants API is deprecated. Responses answers in one call and can
    # search the story vector store from the notebook.
    prompt = body.text
    request = {
        "model": "gpt-4o",
        "instructions": "You are a motivator who answers the question based on the story file",
        "input": prompt,
    }
    if vector_store_id:
        request["tools"] = [{
            "type": "file_search",
            "vector_store_ids": [vector_store_id],
        }]
    response = client.responses.create(**request)
    return {"response": response.output_text}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)