from fastapi import FastAPI , Request , Form , HTTPException , status , Query
from fastapi.responses import HTMLResponse , RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from enum import Enum

app = FastAPI()
app.mount("/static" , StaticFiles ( directory = "static" ) , name = "static")
templates = Jinja2Templates( directory = "templates" )

# @app.get("/index/{id}" , response_class= HTMLResponse )
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request = request , name = "index.html" , context = {"id" : id}
#     )


@app.get("/" , response_class= HTMLResponse )
async def get_signin(request: Request):
    return templates.TemplateResponse(
        request = request , name = "index.html" , context = {"request" : request}
    )

@app.post("/signin/")
async def signin(request : Request , username : Annotated [str , Form()], password : Annotated [str , Form()]):
    print("See signin successful or not?") 
    if username == "test" and password == "test":
        response = RedirectResponse(url="/member" , status_code= status.HTTP_302_FOUND)
        return response
    elif username.strip() == "" or password.strip() == "":
        error_message = "Please enter username and password"
        from urllib.parse import quote
        return RedirectResponse(url = f"/error?message={quote(error_message)}" , status_code = status.HTTP_302_FOUND)
    else:
        error_message = "Username or password is not correct"
        from urllib.parse import quote
        return RedirectResponse(url = f"/error?message={quote(error_message)}" , status_code = status.HTTP_302_FOUND)

@app.get("/member/" , response_class = HTMLResponse )
async def signin_successed(request: Request):
    return templates.TemplateResponse(
        request = request , name = "member.html" , context = {"request" : request}
    )

@app.get("/error" , response_class = HTMLResponse )
async def show_error(request : Request , message : str = ""):
    return templates.TemplateResponse("error.html" , {"request" : request , "error" : message})
