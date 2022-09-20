from typing import Union

from fastapi import FastAPI

app = FastAPI()





@app.get("/ping")
async def ping():
    return "Hellow ,I am working"

#if __name__ == "__main__":
    #uvicorn.run(app, host ='localhost', port=8000)