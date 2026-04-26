from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import json

with open("backend/data/products.json") as f:
    products = json.load(f)

docs = []
for p in products:
    text = f"{p['name']} {p['category']} {p['description']} {p['brand']}"
    docs.append(Document(page_content=text, metadata=p))

embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

def retrieve(query):
    return vectorstore.similarity_search(query, k=3)