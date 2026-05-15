from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Python Task API")


@app.get("/")
def home():
    return {"message": "Python Task API is running"}


app.include_router(tasks.router)
