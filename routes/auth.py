# Only authentication routes
from fastapi import APIRouter, Depends,Request,HTTPException
from database import get_db
from sqlalchemy.orm import Session
import model
from auth_jwt import create_access_token,verify_token
from schma import UserValidator
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
routes=APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"])



@routes.get("/")
def index(request:Request):
   return templates.TemplateResponse("index.html", {"request": request})

@routes.get("/signup")
def signupcheck(request:Request):
   return templates.TemplateResponse("signup.html", {"request": request})

@routes.post("/signup")
def signup(user:UserValidator,db:Session=Depends(get_db)):
    existing_user = db.query(model.User).filter(model.User.phone ==user.phone).first()


    if existing_user:

     raise HTTPException(
        status_code=400,
        detail="Phone already exists"
    )
    hashed = pwd_context.hash(user.password)
   
    new_user=model.User(phone=user.phone,password=hashed)
    db.add(new_user)
    db.commit()       
    return {"msg": "signup done"}

@routes.get("/login")
def logincheck(request:Request):
   return templates.TemplateResponse("login.html", {"request": request})

@routes.post("/login")
def login(user:UserValidator,db:Session=Depends(get_db)):
   
    db_user = db.query(model.User).filter(model.User.phone == user.phone).first()
    if not db_user:
      return {"msg":"user not found"}
    if not pwd_context.verify(user.password, db_user.password):
      return{"msg":"wrong password"}
    token=create_access_token({"sub":db_user.phone})
    return {
        "access_token": token,
        "token_type": "bearer"
    }


@routes.get("/profile")
def profile(data=Depends(verify_token)):
   return{
           
           "user": data
       }


# All other next routes are in dashboard.py file