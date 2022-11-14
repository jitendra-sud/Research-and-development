from fastapi import FastAPI
from routers import user
from urllib import request
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, status, Body
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Prosperity-Backend",description="This contains only Demo API's For Testing Purpose")


app.include_router(user.router, tags=['Users'], prefix='')

app.mount(
    "/static",
    StaticFiles(directory="../onboarding/static"),
    name="static",
)

@app.get("/")
async def root_url():
    return {'message' : "Successfully Running the server..."}



@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}


