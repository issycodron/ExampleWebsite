from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import datetime
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""@app.get("/")
async def homepage(): #async means server can run on multiple threads
    time = datetime.datetime.now()
    return f"the time is {time}"""

@app.get("/", response_class=HTMLResponse) #add /hello at the end of url
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html",{"request": request})


@app.get("/hello/{name}") #app.post submits an entity to the specified resource
async def hello_name(request: Request, name: str):
    return settings.TEMPLATES.TemplateResponse("homepage.html",{"request": request, "name":name})


class SampleInput(BaseModel):
    x: int

@app.post("/sample")
async def sample(input: SampleInput):
    return input.x**2