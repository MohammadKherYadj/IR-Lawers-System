from fastapi import FastAPI
from main import Preprocessing_EN

app = FastAPI()

@app.get("/")
async def index():
    return "OK"

@app.get("/Tokenizer/{text}")
async def tokenizer(text):
    return Preprocessing_EN.process(text)
