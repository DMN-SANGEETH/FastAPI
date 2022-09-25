#from turtle import title
from email.policy import HTTP
from http.client import ACCEPTED, NO_CONTENT, NotConnected
from pyexpat import model
from turtle import title
from urllib import request, response
from fastapi import FastAPI,Depends, status, HTTPException
from . import schemas, models
from .database import SessionLocal, engine ,SessionLocal
from sqlalchemy.orm import Session

import blog

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        

app = FastAPI()

@app.post('/blog', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog =models.Blog(title=request.title, body=request.body)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def distroy(id,  db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    
    if not blogs.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detial=f"Blog with with {id} not found")
        
    blogs.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request: schemas.Blog, db: Session = Depends(get_db) ):
    blogs=db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blogs.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detial=f"Blog with with {id} not found")
    blogs.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'update'
    
    
    
@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code =200)
def show(id,db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id).first()
    
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} is not avilable")
        #response.status_code=status.HTTP_404_NOT_FOUND
    return blogs