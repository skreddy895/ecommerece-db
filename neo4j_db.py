from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USER = "neo4j"
PASSWORD = "your_password"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def test_connection():
    try:
        with driver.session() as session:
            result = session.run("RETURN 'Neo4j Connected' AS msg")
            return {"status": "success", "message": result.single()["msg"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
