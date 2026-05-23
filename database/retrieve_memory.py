import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="./chroma_storage"
)

collection = client.get_or_create_collection(
    name="ai_intelligence_memory"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def search_memory(query):

    embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=5
    )

    return {
    "documents": results["documents"][0],
    "metadata": results["metadatas"][0]
    }