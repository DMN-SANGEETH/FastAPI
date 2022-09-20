from fastapi import FastAPI


app = FastAPI()

@app.post('/blog')
def create(titel,body):
    return {titel:'titel', body:"body"}