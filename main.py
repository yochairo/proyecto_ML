from fastapi import FastAPI
from routers import return_text

app = FastAPI()


app.include_router(return_text.router)

@app.get("/")
def read_root():
    return {"Hello": "World from main"}

