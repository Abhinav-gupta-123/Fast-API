# Here we wil check basic working of endpoints and how to run our api 

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return {"message":"hello world"}
@app.get("/about")
def about():
    return{"message":"A square is an AI agency powered by 2 brothers"}


#to run this api 
#your folder directory then "uvicorn 1_main:app --reload" 