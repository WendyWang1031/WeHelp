from urllib.parse import quote
from fastapi import FastAPI , Request , Form , HTTPException , status , Query , Depends , status
from fastapi.responses import HTMLResponse , RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from db import check_username_exists , insert_new_user
from mysql.connector import cursor
from typing import Annotated

app = FastAPI()
app.mount("/static" , StaticFiles ( directory = "static" ) , name = "static")
app.add_middleware(SessionMiddleware , secret_key = "your-secret-key")
templates = Jinja2Templates( directory = "templates" )

@app.get("/" , response_class= HTMLResponse )
async def get_signin(request: Request):
    return templates.TemplateResponse(
        request = request , name = "index.html" , context = {"request" : request}
    )

@app.get("/signout" , response_class= HTMLResponse )
async def get_signout(request: Request):
    request.session["SIGNED-IN"] = False
    response = RedirectResponse(url="/" , status_code= status.HTTP_302_FOUND)
    response.delete_cookie("session")
    return response

@app.post("/signup" , response_class= HTMLResponse )
async def get_signup( name :  Annotated[str, Form()] , register_username :  Annotated[str, Form()] , register_password :  Annotated[str, Form()]):
    if check_username_exists(register_username) :
        error_message = quote("Repeated username")
        response = RedirectResponse(url = f"/error?message={error_message}" , status_code= status.HTTP_302_FOUND)
        return response
    else:
        insert_new_user(name , register_username , register_password)
        response = RedirectResponse(url="/" , status_code= status.HTTP_302_FOUND)
        return response

@app.post("/signin")
async def signin(request : Request , username :  str = Form(default = "") , password :  str = Form(default = "")  ):
    
    if username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        response = RedirectResponse(url="/member" , status_code= status.HTTP_302_FOUND)
        return response
    elif username.strip() == "" or password.strip() == "":
        error_message = "Please enter username and password"
        response = RedirectResponse(url = f"/error?message={quote(error_message)}" , status_code = status.HTTP_302_FOUND)
        return response
    else:
        error_message = "Username or password is not correct"
        response = RedirectResponse(url = f"/error?message={quote(error_message)}" , status_code = status.HTTP_302_FOUND)
        return response

    

@app.get("/member" , response_class = HTMLResponse )
async def signin_successed(request: Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        return templates.TemplateResponse(
            request = request , name = "member.html" , context = {"request" : request}
    )
    else:
        return RedirectResponse(url = "/" , status_code = status.HTTP_302_FOUND)

@app.get("/error" , response_class = HTMLResponse )
async def show_error(request : Request , message : str = ""):
    return templates.TemplateResponse("error.html" , {"request" : request , "message" : message})

@app.get("/square/{cal}" , response_class = HTMLResponse )
async def square_math(request : Request , cal : int):
    result = cal * cal
    return templates.TemplateResponse("square.html" , {"request" : request , "result" : result})

# 使用post來渲染數字頁面
# @app.post("/calculate/")
# async def calculate_square( number : int = Form(default = 0)):
    
#     response = RedirectResponse(url=f"/square/{number}" , status_code= status.HTTP_302_FOUND)
#     return response