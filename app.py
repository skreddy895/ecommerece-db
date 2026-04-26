from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from graph.neo4j_db import test_connection, get_products_by_category, get_all_products

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 Serve frontend (IMPORTANT)
app.mount("/static", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/test-db")
def test_db():
    return test_connection()


@app.get("/products")
def products():
    return {"data": get_all_products()}


@app.get("/chat")
def chat(query: str):
    query = query.lower()

    category_map = {
        "mobile": ["mobile", "phone"],
        "laptop": ["laptop"],
        "shoes": ["shoes"],
        "watch": ["watch"]
    }

    for cat, words in category_map.items():
        if any(w in query for w in words):
            return {
                "answer": f"{cat} products found",
                "data": get_products_by_category(cat)
            }

    return {
        "answer": "showing products",
        "data": get_all_products()
    }