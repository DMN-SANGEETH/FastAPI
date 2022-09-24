#from turtle import title
from turtle import title
from urllib import response
from fastapi import FastAPI,Depends, status, HTTPException
from . import schemas, models
from .database import SessionLocal, engine ,SessionLocal
from sqlalchemy.orm import Session

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