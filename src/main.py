from fastapi import FastAPI

from .middleware.cors import setup_cors

app = FastAPI()

setup_cors(app)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
