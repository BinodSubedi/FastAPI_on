from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Binod'}}

@app.get('/about')
def about():
    return {'data':{'about':'fastAPI'}}