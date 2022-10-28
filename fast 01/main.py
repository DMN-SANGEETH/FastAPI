

from turtle import title
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def index(limit=10, published : bool=True, sort: Optional[str] =None):
    if published:
        return{'data': f'{limit} published blog from the db'}
    else:
        return{'data': f'{limit} published blog from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return{'data':'all unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def creat_blog(blog: Blog):
    
    return{'data':f'blog is creat whith titel as {blog.title}'}

#@app.post('/blog/do')
#def frist():
    #return {'data':'first one'}



