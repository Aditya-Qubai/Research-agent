import fitz
import tempfile


async def extract_pdf_text(file):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:

        contents = await file.read()
        temp_pdf.write(contents)
        temp_path = temp_pdf.name

    doc = fitz.open(temp_path)

    extracted_text = ""

    for page in doc:
        extracted_text += page.get_text()

    doc.close()

    return extracted_text