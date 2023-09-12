from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import uvicorn

from os import environ as env

app = FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
    
# @app.get("/")
# def index():
#     return {"data": f"Hello {env['MY_NAME_VARIABLE']}!!!"}


@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("base.html",{"request":request})

@app.get("/login")
async def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)