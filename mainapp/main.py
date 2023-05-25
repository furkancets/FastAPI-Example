from fastapi import FastAPI
from mainapp.database import engine
from mainapp.routers import customer, user
from sqlmodel import SQLModel


app = FastAPI()
app.include_router(customer.router)
app.include_router(user.router)

# Creates all tables
# Create Database and Tables on startup
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)