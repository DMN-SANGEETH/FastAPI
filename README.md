@app.get('/user/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id==id).first()
    
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not avilable")
        #response.status_code=status.HTTP_404_NOT_FOUND
    return users 


@app.post('/user')
def creat_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user =models.User(name=request.name, password=Hash.bcrypt(request.password), email=request.email)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 
