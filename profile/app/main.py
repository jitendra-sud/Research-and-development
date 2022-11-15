from  urllib  import  request
from  fastapi  import  FastAPI, Request
from  app.routers  import  coverage, feedback, personal_details,documents, manage_payments, notification
from  fastapi.staticfiles  import  StaticFiles

app  = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

app.include_router(feedback.router)
app.include_router(personal_details.router)
app.include_router(documents.router)
app.include_router(manage_payments.router)
app.include_router(notification.router)
app.include_router(coverage.router)

@app.get("/")
def show():
    return {"data":"This is Prosperity profile API."}



# ###########################################

