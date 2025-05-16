#!/opt/homebrew/bin/python3

#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world(param1, param2):
    a = 1
    return f"Hello, World! {a + 1}, param1: {param1}, param2: {param2}"
