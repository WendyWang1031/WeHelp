from urllib.parse import quote
from fastapi import FastAPI , Request , Form , HTTPException , status , Query , Depends , status
from fastapi.responses import HTMLResponse , RedirectResponse , JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from db import check_username_exists , insert_new_user  , check_username_password , get_user_by_username_password , get_all_messages , insert_message , delete_message , is_user_message_owner , get_member_details, update_user_name
from mysql.connector import cursor
from typing import Annotated , Optional
import json
from pydantic import BaseModel

class LoginData(BaseModel):
    username: str
    password: str

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

@app.get("/api/member" , response_class = JSONResponse )
async def get_member_data(request: Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        user_name = request.session.get("name")
        user_id = request.session.get("id")
        messages = get_all_messages()
        response = JSONResponse(
            status_code = status.HTTP_200_OK,
            content={
            "success":True,
            "user_id":user_id,
            "user_name":user_name,
            "message":messages
        })
        return response
    else:
        return RedirectResponse(url = "/" , status_code = status.HTTP_302_FOUND)

@app.get("/api/user" , response_class=JSONResponse)
async def get_user_info(request: Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        user_name = request.session.get("name")
        return {"user_name" : user_name}
    else:
        raise HTTPException(status_code=401 , detail="User not signed in.")





@app.get("/api/member_username" , response_class = JSONResponse )
async def demand_username(request: Request , username : Optional[str] = None):
    if "SIGNED-IN" not in request.session or not request.session["SIGNED-IN"]:
        response = JSONResponse(
            status_code = status.HTTP_401_UNAUTHORIZED,
            content = {"success":False ,"data": None , "message": "User is not signed in"}
        )
        return response
    if not username:
        response = JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {"success":False ,"data": None , "message": "Username parameter is missing"}
        )
        return response

    member_data = get_member_details(username)
    if member_data:
        data_dict = dict (zip(["id" , "name" , "username"], member_data ))
        response = JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {"success":True ,"data" : data_dict}
    )
        return response
    else:
        response = JSONResponse(
        status_code = status.HTTP_404_NOT_FOUND,
        content = {"success":False ,"data": None, "message": "Member not found"}
    )
        return response
    
    
    
        


@app.patch("/api/member" , response_class = JSONResponse )
async def change_username(request: Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        json_body = await request.json()
        print(json_body)
        name = json_body.get("name")
        if name and isinstance(name, str):
            user_id = request.session.get("id")
            update_success = update_user_name(user_id , name)
            if update_success:
                response = JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"success":True,"message":"Updated sucessful!"} 
                )
                return response
            else:
                response = JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"success":False , "message":"Updated failed. User not found."}
                )
                return response
        else:
            response = JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"success":False , "message":"Name parameter is missing or invalid."}
                )
            return response
        
    else:
        response = JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"success":False , "message":"User is not signed in."}
                )
        return  response



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

@app.post("/api/signup" , response_class = JSONResponse )
async def signup(request : Request):
    json_body = await request.json()
    name = json_body.get("name")
    username = json_body.get("username")
    password = json_body.get("password")

    username_exists = check_username_exists(username)
    
    if username_exists is True :
        response = JSONResponse(content={"success":False , "message":"Repeated username"} , status_code=status.HTTP_401_UNAUTHORIZED)
        return response
    elif username_exists is False:
        if insert_new_user(name , username , password):
            response = JSONResponse(content={"success":True , "redirect":"/"} , status_code=status.HTTP_200_OK)
            return response
        else:
            response = JSONResponse(content={"success":False , "message":"Failed to create user due to a server error"} , status_code=status.HTTP_401_UNAUTHORIZED)
            return response
    else:
        response = JSONResponse(content={"success":False , "message":"Failed to perform th check due to a database error"} , status_code=status.HTTP_401_UNAUTHORIZED)
        return response


@app.post("/api/login", response_class= JSONResponse)
async def login(request : Request):
    json_body = await request.json()
    username = json_body.get("username")
    password = json_body.get("password")

    if check_username_password(username , password):
        user_record = get_user_by_username_password(username , password)
        if user_record:
            request.session["SIGNED-IN"] = True
            request.session["name"] = user_record["name"]
            request.session["id"] = user_record["id"]
            response = JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"success":True , "redirect":"/member"} 
                )
            return response
        else:
            response = JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"success":False , "message":"Failed to retrieve user details"}
                )
                
            return response
    
    else:
        response = JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"success":False , "message":"Username or password is not correct"}
            )
        return response

@app.post("/api/message" , response_class= JSONResponse)
async def message_input_output( request : Request):
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        json_body = await request.json()
        message_content = json_body.get("content")
        
        user_id = request.session.get("id")
        if message_content:
            success =  insert_message(user_id , message_content)
            if success:
                response = JSONResponse(
                    status_code= status.HTTP_201_CREATED , 
                    content={"success":True , "message" : "Message added successfully"}
                    )
                return response
            else:
                response = JSONResponse( 
                    status_code= status.HTTP_400_BAD_REQUEST , 
                    content={"success":False , "message":"Failed to add message"}
                    )
                return response
        else:
            response = JSONResponse( 
                status_code= status.HTTP_400_BAD_REQUEST , 
                content={"success":False , "message" : "No message content provided"}
                )
            return response
    else:
        response = JSONResponse( 
            status_code= status.HTTP_401_UNAUTHORIZED , 
            content={"success":False , "message":"User not signed in"}
            )
        return response

@app.post("/deleteMessage" , response_class= HTMLResponse)
async def message_delete( request : Request , message_id :  int = Form(...)):
    
    if "SIGNED-IN" in request.session and request.session["SIGNED-IN"]:
        user_id = request.session.get("id")
        if is_user_message_owner(user_id , message_id):
            success = delete_message(message_id)
            if success:
                return RedirectResponse(url= "/member" , status_code= status.HTTP_302_FOUND)
            else:
                return RedirectResponse(url= "/member" , status_code= status.HTTP_302_FOUND)
        else:
            return RedirectResponse(url= "/member" , status_code= status.HTTP_403_FORBIDDEN)
    
    else:
        return RedirectResponse(url= "/" , status_code= status.HTTP_302_FOUND)


