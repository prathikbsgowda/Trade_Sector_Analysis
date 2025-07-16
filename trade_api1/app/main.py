from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="Trade Opportunities API")
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

