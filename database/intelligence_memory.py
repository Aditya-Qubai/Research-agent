import chromadb
from sentence_transformers import SentenceTransformer
from datetime import datetime


client = chromadb.PersistentClient(path="./chroma_storage")

collection = client.get_or_create_collection(
    name="ai_intelligence_memory"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def store_intelligence(title, content, source="rss"):

    combined = f"{title}\n\n{content}"

    embedding = embedding_model.encode(
        combined
    ).tolist()

    unique_id = (
        title[:30]
        + "_"
        + str(datetime.utcnow().timestamp())
    )

    collection.add(
        documents=[combined],

        embeddings=[embedding],

        ids=[unique_id],

        metadatas=[{
            "title": title,
            "source": source,
            "timestamp": str(datetime.utcnow())
        }]
    )