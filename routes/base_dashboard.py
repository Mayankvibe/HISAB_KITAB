from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from schma import CustomerValidator
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
import model
from auth_jwt import verify_token

templates = Jinja2Templates(directory="templates")
routes=APIRouter()




@routes.get("/dashboard")
def dashboard(request:Request):
   return templates.TemplateResponse("dashboard.html",{"request":request})


@routes.post("/dashboard")
def dashboard(request:Request,db:Session=Depends(get_db),data=Depends(verify_token)):
   print("DASHBOARD ROUTE HIT")
   user_phone=str(data["sub"])

   user=db.query(model.User).filter(model.User.phone==user_phone).first()
   customers=db.query(model.Customer).filter(model.Customer.user_id==user.id).all()
   customer_count=len(customers)
   total_amount=sum(c.amount for c in customers)
   print(customer_count)
   print(total_amount)
   return templates.TemplateResponse("dashbored.html",{"request":request,"customer_count":customer_count,"total_amount":total_amount})


@routes.get("/search")
def search(name:str=None,

date:str=None,

db:Session=Depends(get_db)):
   
 customers=db.query(
model.Customer
)

 if name:

     customers=customers.filter(
        model.Customer.name.contains(
            name
        )
    )



 customers=customers.all()

 return [

{

"name":c.name,

"phone":c.phone,

"amount":c.amount

}

for c in customers

]


@routes.get("/customer")
def a_customer(request:Request):
      return templates.TemplateResponse("customer.html",{"request":request})

@routes.post("/customer")
def add_customer(customer:CustomerValidator,db:Session=Depends(get_db),data=Depends(verify_token)):
      user_phone=str(data["sub"])

      user = db.query(
         model.User
      ).filter(
         model.User.phone == user_phone
      ).first()


      new_customer = model.Customer(

         user_id=user.id,

         name=customer.name,

         phone=customer.phone,

         amount=customer.amount,
        
         mode=customer.mode

      )


      db.add(
         new_customer
      )

      db.commit()


      return {

         "msg":"Customer added"

      }
   
  