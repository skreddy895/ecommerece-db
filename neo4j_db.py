import os
from neo4j import GraphDatabase

URI = os.getenv("neo4j+s://e48f68d5.databases.neo4j.io")
USERNAME = os.getenv("neo4j")
PASSWORD = os.getenv("_CYFAJRCOm5tMXTJhP2WRek2-yt5HAS6A7WKyDsQtxM")

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected' AS msg")
        return result.single()["msg"]


def get_products_by_category(category):
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


def get_all_products():
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