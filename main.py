from fastapi import FastAPI, UploadFile, File

from services.pdf_service import extract_pdf_text
from services.embedding_service import (
    chunk_text,
    create_embeddings
)

from database.chroma_db import collection

from agents.workflow import research_workflow

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Research Agent Running"}


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    # Extract text
    extracted_text = await extract_pdf_text(file)

    # Chunk text
    chunks = chunk_text(extracted_text)

    # Create embeddings
    embeddings = create_embeddings(chunks)

    # Store in memory
    for idx, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[idx]],
            ids=[f"{file.filename}_{idx}"]
        )

    # AI summary
    # Run LangGraph workflow
    result = research_workflow.invoke({
    "text": extracted_text
    })

    return {
    "filename": file.filename,
    "chunks_stored": len(chunks),
    "summary": result["summary"],
    "critique": result["critique"],
    "concepts": result["concepts"]
    }