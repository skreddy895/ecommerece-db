from neo4j import GraphDatabase

URI = "neo4j://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "karthik@123"

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
