from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=['类别1'])
async def root():
    return {"message": "Hello World"}


@app.post("/", tags=['类别2'])
async def post_root():
    return {"message": "Hello World"}