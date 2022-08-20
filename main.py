from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data":
                {"name": "hello", "age": 10},
            "meta":
                {"version": "123"}}
