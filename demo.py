import os
from typing import Union
from fastapi import FastAPI
from huggingface_hub import InferenceClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# client = InferenceClient(model="HuggingFaceTB/SmolLM-135M", token=os.getenv('HFTOKEN'))
client = InferenceClient(model="gpt2", token=os.getenv('HFTOKEN'))
app = FastAPI()


# print(app)

@app.get("/")
async def root():
    return {"message":"hello thanga"}

@app.get("/hello/")
async def root():
    time = datetime.now()
    return {"message":"Once again a hello",
            "time is": time}

@app.get("/time")
async def time():
    time = datetime.now()
    return {
        "hey" : "hello, welcome again",
        "time is" : time
    }

@app.get("/get_token")
async def token():
    token = os.getenv('HFTOKEN')
    print(token)
    return {
        "token - ": token
    }

# lets say to get the cli / client details

@app.get("/cli/details/")
async def details():
    return {
        "Client Info -": client
    }

# generate default text with given prompt
@app.get("/generate")
async def gen(prompt):
    prompt = "India is a country known for its spices and"
    response = client.text_generation(prompt)
    return {
        "prompt" : prompt,
        "response" : response
    }


@app.get("/converse")
async def converse(prompt : Union[str,None]): # type annotations
                                              # Union tells this or that (string or empty)
    prompt = prompt or "Indian is known for"
    response = client.text_generation(prompt)
    return {
        "prompt" : prompt,
        "response" : response
    }
