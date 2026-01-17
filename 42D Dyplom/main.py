from collections import namedtuple
from dataclasses import dataclass
import os
import re
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


@dataclass
class BibleVerse:
    book: str
    chapter: str
    verse: str
    text: str


current_dir = os.path.dirname(os.path.abspath(__file__))
file_name: str = "Bible.txt"
file_path: str = os.path.join(current_dir, file_name)

bare_lines = []
typed_lines = []
with open(file_path, encoding="utf-8", mode="r") as f:
    for line in f.readlines():
        line = line.strip()
        bare_lines.append(line)

        regex_pattern = r"(\w+)\s+(\d+:\d+)\s"
        match = re.search(regex_pattern, line)
        if match:
            book = match.group(1)
            chapter_verse = match.group(2)
            chapter, verse = chapter_verse.split(":")
            text = line.replace(match.group(0), "")
            typed_lines.append(BibleVerse(book, chapter, verse, text))


model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for the documents
document_embeddings = model.encode(bare_lines)

# Convert embeddings to a NumPy array
document_embeddings_np = np.array(document_embeddings)

# Create a FAISS index using L2 distance
index = faiss.IndexFlatL2(document_embeddings_np.shape[1])
index.add(document_embeddings_np)

# Define a search query
query = "Ісус Господь"

# Create an embedding for the query
query_embedding = model.encode([query])

# Perform the search, retrieving the top 3 closest matches
k = 10
distances, indices = index.search(query_embedding, k)

# Display the results
print("Query:", query)
print("\nTop", k, "most similar documents:")
for i in range(k):
    print(f"{bare_lines[indices[0][i]]}")
