from fastapi import FastAPI, Request
import datetime
from fastapi.responses import HTMLResponse

from . import settings

app = FastAPI()

"""@app.get("/")
async def homepage(): #async means server can run on multiple threads
    time = datetime.datetime.now()
    return f"the time is {time}"""

@app.get("/", response_class=HTMLResponse) #add /hello at the end of url
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html",{"request": request})


@app.get("/hello/{name}")
async def hello_name(name: str):
    return f"Hello, {name}"