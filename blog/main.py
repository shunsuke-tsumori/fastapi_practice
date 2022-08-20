from fastapi import FastAPI

from blog.schemas import Blog

app = FastAPI()


@app.post("/blog")
def post_blog(blog: Blog):
    return "create"
