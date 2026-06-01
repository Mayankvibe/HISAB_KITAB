from sqlalchemy import Integer,String,Column
from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    id=Column("id",Integer,primary_key=True,index=True)
    phone=Column("phone",String,unique=True,nullable=False)
    password=Column("password",String,nullable=False)
    customer=relationship("Customer",back_populates="user")
class Customer(Base):
    __tablename__="customer"
    id=Column("id",Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    name=Column(String,nullable=False)
    phone=Column(String,nullable=False)
    amount=Column(String,nullable=False)
    mode=Column(String,nullable=False)
    user=relationship("User",back_populates="customer")