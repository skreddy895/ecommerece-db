from fastapi import FastAPI
import json
from neo4j_db import test_connection

app = FastAPI()

# Load products
with open("products.json", "r") as f:
    products = json.load(f)

@app.get("/")
def home():
    return {"message": "Server is working"}

@app.get("/products")
def get_products():
    return products

@app.get("/test-db")
def test_db():
    return test_connection()
