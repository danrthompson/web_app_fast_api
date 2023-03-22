# from deta import App
from fastapi import FastAPI

# from fastapi.responses import JSONResponse

# from pydantic import BaseModel


# app = App(FastAPI())
app = FastAPI()


# @app.get("/", response_class=JSONResponse)
@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.lib.cron()
# def cron_job(event):
#     return "Hello Deta, I am a cron job"
