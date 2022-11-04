from fastapi import FastAPI, Depends, status
from . import schemas,models
from .database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = sessionLocal()
    
    try:
        yield db
    finally:
        db.close()
    


@app.post('/blog', status_code=status.HTTP_201_CREATED, response_model=schemas.CreateShow)
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

        