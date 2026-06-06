from pydantic import BaseModel,field_validator

class UserValidator(BaseModel):


    phone: str
    password: str

    @field_validator("password")
    def check_password(cls, v):
        if len(v) < 6:
            raise ValueError("Password too short atleast 6 digit")
        return v
    @field_validator("phone")
    def check_phone(cls,p):
        if not p.isdigit():
            raise ValueError("Phone must contain only numbers")
        if len(str(p))!= 10:
            raise ValueError("phone must be 10 digit")
        return p
    
class CustomerValidator(BaseModel):

    name:str
    phone:str
    amount:int
    mode:str

    @field_validator("phone")
    def check_phone(cls,p):
        if not p.isdigit():
            raise ValueError("Phone must contain only numbers")
        if len(str(p))!= 10:
            raise ValueError("phone must be 10 digit")
        return p
    
    @field_validator("amount")    
    def check_amount(cls,a):
        if a<0:
            raise ValueError("Amount cannot be negative")
        return a