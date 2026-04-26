# graph/neo4j_db.py

def test_connection():
    return "Neo4j disabled for deployment"

def get_products_by_category(category):
    return [
        {
            "name": "iPhone 14",
            "category": "mobile",
            "price": 70000,
            "image": "https://via.placeholder.com/150"
        },
        {
            "name": "Dell Laptop",
            "category": "laptop",
            "price": 55000,
            "image": "https://via.placeholder.com/150"
        }
    ]

def get_all_products():
    return [
        {
            "name": "iPhone 14",
            "category": "mobile",
            "price": 70000,
            "image": "https://via.placeholder.com/150"
        },
        {
            "name": "Dell Laptop",
            "category": "laptop",
            "price": 55000,
            "image": "https://via.placeholder.com/150"
        },
        {
            "name": "Boat Headphones",
            "category": "accessories",
            "price": 2000,
            "image": "https://via.placeholder.com/150"
        }
    ]