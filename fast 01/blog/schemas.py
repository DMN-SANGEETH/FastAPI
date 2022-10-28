
import email
from os import name
from turtle import title
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        orm_model=True
    

# class Blog(BaseModel):
#     title: str
#     body: str
    
# class ShowBlog(BaseModel):
#     title: str
#     body: str
#     class Config():
#         orm_model=True
        


    
   