from urllib import request
from fastapi import FastAPI
from app import schemas
from app.schemas import Feedback, ShowFeedback
from app.routers import coverage, feedback, personal_details,documents, manage_payments, notification
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, status, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


# templates = Jinja2Templates(directory="templates")


app  = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# @app.get("/profileDetails", response_model = schemas.ShowPersonalDetails)
# async def show( request: Request):
#     context = {'request': request}
#     return templates.TemplateResponse("profiles/profileDetails.html",context)

# @app.post("/profileDetails")
# async def create(request: Request, name: str = Form(...), number: int = Form(...), email: str = Form(...), profession: str = Form(...) ):
#     result = ({
#         'name': name,
#         'number': number,
#         'email': email,
#         'profession': profession
#     })
#     # context = {'request':request, 'result':result}
#     return result

app.include_router(feedback.router)
app.include_router(personal_details.router)
app.include_router(documents.router)
app.include_router(manage_payments.router)
app.include_router(notification.router)
app.include_router(coverage.router)

@app.get("/")
def show():
    return {"data":"This is Prosperity profile API."}