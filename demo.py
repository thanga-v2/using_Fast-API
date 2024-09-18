import os
from typing import Union
from fastapi import FastAPI
from huggingface_hub import InferenceClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(model="groq", token=os.getenv('HFTOKEN'))
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