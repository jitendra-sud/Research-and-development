from fastapi import APIRouter

defaultRoute = APIRouter()

class UsersRoute:
    route = APIRouter()
    base = '/users/'
    UploadImage = f'{base}image-upload/'


