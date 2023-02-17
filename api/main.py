from fastapi import FastAPI
import datetime
from fastapi.responses import HTMLResponse

app = FastAPI()

"""@app.get("/")
async def homepage(): #async means server can run on multiple threads
    time = datetime.datetime.now()
    return f"the time is {time}"""

@app.get("/", response_class=HTMLResponse) #add /hello at the end of url
async def hello():
    return f"<h1>Hello, world!</h1>"

@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}"