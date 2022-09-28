
from os import name
from turtle import title
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel ):
    title: str
    body: str
    class Config():
        orm_model=True
        
class User(BaseModel ):
    name: str
    email: str
    pasword: str
   