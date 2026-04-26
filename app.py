from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ FIXED IMPORT (NO "graph" folder)
from neo4j_db import (
    test_connection,
    get_products_by_category,
    get_all_products
)

app = FastAPI()

# Allow frontend (important for Render + browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "Server working 🚀"}

# ---------------- TEST DB ----------------
@app.get("/test-db")
def test_db():
    try:
        return {"status": test_connection()}
    except Exception as e:
        return {"error": str(e)}

# ---------------- ALL PRODUCTS ----------------
@app.get("/products")
def products():
    try:
        return {"data": get_all_products()}
    except Exception as e:
        return {"error": str(e)}

# ---------------- CHAT / SEARCH ----------------
@app.get("/chat")
def chat(query: str):
    query = query.lower()

    category_map = {
        "mobile": ["mobile", "phone", "iphone"],
        "laptop": ["laptop", "dell", "hp"],
        "shoes": ["shoes"],
        "watch": ["watch"],
        "accessories": ["headphones", "earbuds"]
    }

    # category detection
    for cat, words in category_map.items():
        if any(w in query for w in words):
            return {
                "answer": f"{cat} products found",
                "data": get_products_by_category(cat)
            }

    # fallback
    return {
        "answer": "showing all products",
        "data": get_all_products()
    }