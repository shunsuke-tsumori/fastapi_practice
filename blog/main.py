from fastapi import FastAPI, Depends

from . import models
from .schemas import Blog
from .models import Base
from .database import engine, session_local
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(engine)


# リクエストごとにセッションを作成する常套句
def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def post_blog(blog: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog")
def all_getch(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}")
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
