import chromadb

client = chromadb.Client()

collection = client.create_collection("research_papers")