from fastapi import FastAPI

from .auth.routes import router as auth_router
from .bank.routes import router as bank_router
from .middleware.cors import setup_cors
from .user.routes import router as user_router

app = FastAPI()

setup_cors(app)

app.include_router(auth_router, prefix="/api")
app.include_router(bank_router, prefix="/api")
app.include_router(user_router, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
