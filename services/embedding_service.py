from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=500):

    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


def create_embeddings(chunks):

    return model.encode(chunks).tolist()