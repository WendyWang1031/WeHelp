from urllib.parse import quote
from fastapi import FastAPI , Request , Form , HTTPException , status , Query , Depends , status
from fastapi.responses import HTMLResponse , RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from db import check_username_exists , insert_new_user  , check_username , get_all_messages , insert_message , delete_message , is_user_message_owner
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
    username_exists = check_username_exists(register_username)
    
    if username_exists is True :
        error_message = quote("Repeated username")
        response = RedirectResponse(url = f"/error?message={error_message}" , status_code= status.HTTP_302_FOUND)
        return response
    elif username_exists is False:
        if insert_new_user(name , register_username , register_password):
            response = RedirectResponse(url="/" , status_code= status.HTTP_302_FOUND)
            return response
        else:
            error_message = quote("Failed to create user due to a server error")
            response = RedirectResponse(url = f"/error?message={error_message}" , status_code= status.HTTP_302_FOUND)
            return response
    else:
        error_message = quote("Failed to perform th check due to a database error")
        response = RedirectResponse(url = f"/error?message={error_message}" , status_code= status.HTTP_302_FOUND)
        return response




    

@app.post("/signin")
async def signin(request : Request , username :  str = Form(default = "") , password :  str = Form(default = "")  ):
    user_record = check_username(username , password)
    if user_record:
        request.session["SIGNED-IN"] = True
        request.session["name"] = user_record["name"]
        request.session["id"] = user_record["id"]
        response = RedirectResponse(url="/member" , status_code= status.HTTP_302_FOUND)
        return response
    
    else:
        error_message = "Username or password is not correct"
        response = RedirectResponse(url = f"/error?message={quote(error_message)}" , status_code = status.HTTP_302_FOUND)
        return response

    

@app.get("/member" , response_class = HTMLResponse )
async def signin_successed(request: Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        user_name = request.session.get("name")
        user_id = request.session.get("id")
        show_message = get_all_messages()
        return templates.TemplateResponse(
            request = request , 
            name = "member.html" , 
            context = {"request" : request , "user_id" : user_id , "user_name" : user_name , "show_message" : show_message}
    )
    else:
        return RedirectResponse(url = "/" , status_code = status.HTTP_302_FOUND)
    


@app.get("/error" , response_class = HTMLResponse )
async def show_error(request : Request , message : str = ""):
    return templates.TemplateResponse("error.html" , {"request" : request , "message" : message})

@app.post("/createMessage" , response_class= HTMLResponse)
async def message_input_output( request : Request , message_content :  str = Form(default = "") ):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        user_id = request.session.get("id")
        if message_content:
            insert_message(user_id , message_content)
            return RedirectResponse(url= "/member" , status_code= status.HTTP_302_FOUND)
        else:
            return RedirectResponse(url= "/member" , status_code= status.HTTP_302_FOUND)
    else:
        return RedirectResponse(url= "/" , status_code= status.HTTP_302_FOUND)
    


@app.post("/deleteMessage" , response_class= HTMLResponse)
async def message_delete( request : Request , message_id :  int = Form(...)):
    
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        user_id = request.session.get("id")
        if is_user_message_owner(user_id , message_id):
            delete_message(message_id)
            return RedirectResponse(url= "/member" , status_code= status.HTTP_302_FOUND)
        else:
            return RedirectResponse(url= "/member" , status_code= status.HTTP_403_FORBIDDEN)
    
    else:
        return RedirectResponse(url= "/" , status_code= status.HTTP_302_FOUND)


    

# @app.get("/square/{cal}" , response_class = HTMLResponse )
# async def square_math(request : Request , cal : int):
#     result = cal * cal
#     return templates.TemplateResponse("square.html" , {"request" : request , "result" : result})


