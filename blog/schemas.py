import pydantic


class Blog(pydantic.BaseModel):
    title: str
    body: str
