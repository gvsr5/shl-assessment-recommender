
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("shl_catalog.json", "r") as f:
    catalog = json.load(f)

descriptions = [item["description"] for item in catalog]
embeddings = model.encode(descriptions, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def get_recommendations(query, k=10):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        item = catalog[idx]
        results.append({
            "Assessment Name": item["name"],
            "URL": item["url"],
            "Remote Testing": item["remote_testing"],
            "Adaptive/IRT": item["adaptive"],
            "Duration": item["duration"],
            "Test Type": item["test_type"]
        })
    return results
