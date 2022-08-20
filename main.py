from typing import Optional

import pydantic
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data":
                {"name": "hello", "age": 10},
            "meta":
                {"version": "123"}}


@app.get("/blog/{id}/comments")
def get_comments(id: int):
    return {"data": {id, "comments"}}


@app.get("/blog")
def get_item(limit: int = 10, published: bool = True):
    if published:
        return {"data": f"{limit}件"}
    else:
        return {"data": "not found"}


class Blog(pydantic.BaseModel):
    title: str
    description: str
    published_at: Optional[bool]


@app.post("/blog")
def post_blog(blog: Blog):
    return {"data": blog}
