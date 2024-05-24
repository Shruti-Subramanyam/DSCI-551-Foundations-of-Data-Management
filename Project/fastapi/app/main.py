from typing import Union
from fastapi import FastAPI
from pymongo import MongoClient
from app.routes_farmer import router as farmer_router
from app.routes_user import router as user_router
import os

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb0_client = MongoClient(os.getenv("MDB0_URI"))
    app.mongodb1_client = MongoClient(os.getenv("MDB1_URI"))
    app.database0 = app.mongodb0_client[os.getenv("DB_NAME")]
    app.database1 = app.mongodb1_client[os.getenv("DB_NAME")]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(farmer_router, tags=["farmers"], prefix="/farmer")
app.include_router(user_router, tags=["users"], prefix="/user")
