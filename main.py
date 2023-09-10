from fastapi import FastAPI
import uvicorn

from os import environ as env


app = FastAPI()

@app.get("/")
def index():
    return {"data": f"Hello {env['MY_NAME_VARIABLE']}!!!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)