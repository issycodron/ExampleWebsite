from fastapi import FastAPI
import datetime

app = FastAPI()

"""@app.get("/")
async def homepage(): #async means server can run on multiple threads
    time = datetime.datetime.now()
    return f"the time is {time}"""

@app.get("/hello") #add /hello at the end of url
async def hello():
    return f"Hello, world!"

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}"