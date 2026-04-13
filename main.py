from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates 

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
def intro(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/signup")
def signup_page(request:Request):
    return templates.TemplateResponse("signup.html",{"request":request})

users={}
@app.post("/signup", status_code=201,)
def signup(phone: str = Form(...), password: str = Form(...)):
    users[phone] = password
    return templates.TemplateResponse("signup.html",{"request":request , "msg":"done signup "})

@app.post("/login", status_code=201)
def create(phone: str = Form(...), password: str = Form(...)):
    pass