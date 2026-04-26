from neo4j import GraphDatabase
import os

# -----------------------------
# 🔥 USE ENV VARIABLES (BEST PRACTICE FOR RENDER)
# -----------------------------
URI = os.getenv("NEO4J_URI", "neo4j+s://e48f68d5.databases.neo4j.io")
USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "_CYFAJRCOm5tMXTJhP2WRek2-yt5HAS6A7WKyDsQtxM")

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


# -----------------------------
# TEST CONNECTION
# -----------------------------
def test_connection():
    try:
        with driver.session() as session:
            result = session.run("RETURN 'Connected' AS msg")
            return result.single()["msg"]
    except Exception as e:
        return f"Connection failed: {str(e)}"


# -----------------------------
# GET PRODUCTS BY CATEGORY
# -----------------------------
def get_products_by_category(category):
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (p:Product)
                WHERE toLower(p.category) CONTAINS toLower($category)
                RETURN p.name AS name,
                       p.price AS price,
                       p.category AS category,
                       p.image AS image
                LIMIT 20
                """,
                category=category
            )
            return [record.data() for record in result]
    except Exception as e:
        return [{"error": str(e)}]


# -----------------------------
# GET ALL PRODUCTS
# -----------------------------
def get_all_products():
    try:
        with driver.session() as session:
            result = session.run(
                """
                MATCH (p:Product)
                RETURN p.name AS name,
                       p.price AS price,
                       p.category AS category,
                       p.image AS image
                LIMIT 40
                """
            )
            return [record.data() for record in result]
    except Exception as e:
        return [{"error": str(e)}]