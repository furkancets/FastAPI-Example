from sqlmodel import SQLModel, Field
from typing import Optional


class Customer(SQLModel, table=True):
    customerId: Optional[int] = Field(default=None, primary_key=True)
    customerFName: str
    customerLName: str
    customerEmail: str
    customerPassword: str
    customerStreet: str
    customerCity: str
    customerState: str
    customerZipcode: str
    
    """
    customerId,customerFName,customerLName,customerEmail,customerPassword,customerStreet,customerCity,customerState,customerZipcode
    1,Richard,Hernandez,XXXXXXXXX,XXXXXXXXX,6303 Heather Plaza,Brownsville,TX,78521
    """
    
class CreateUpdateCustomer(SQLModel):
    customerFName: str
    customerLName: str
    customerEmail: str
    customerPassword: str
    customerStreet: str
    customerCity: str
    customerState: str
    customerZipcode: str


class ShowCustomer(SQLModel):
    customerFName: str
    customerLName: str
    customerEmail: str
    customerStreet: str
    customerCity: str
    customerState: str
    customerZipcode: str


class Login(SQLModel):
    username: str
    password: str


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: str
    email: str
    password: str
    
    
class CreateUpdateUser(SQLModel):
    name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "username": "john1",
                "email": "john1@example.local",
                "password": "strongPassword"
            }
        }
        
        
class ShowUser(SQLModel):
    name: str
    email: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john1@example.local"
            }
        }
