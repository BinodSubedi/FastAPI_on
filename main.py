from tokenize import String
from typing import Optional
from fastapi import FastAPI
import uvicorn
from .blog import schemas

app = FastAPI()

@app.get('/blog')
# default value
def index(limit=10, published: str ='published',sort: Optional[str] = None):
    return {'data':f'Blog list with {limit} blogs which are {published}'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'All un-published data'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'},
            'id':id}


 
@app.post('/blog')
def create_blog(request:schemas.Blog):
    # return request
    return {'data':f'Blog Created! it\'s with title {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=8080)