import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(query):
    doc = nlp(query)

    entities = {
        "product": [],
        "brand": [],
        "price": []
    }

    for token in doc:
        if token.pos_ == "PROPN":
            entities["product"].append(token.text)

        if token.like_num:
            entities["price"].append(token.text)

    return entities