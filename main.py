from fastapi import FastAPI, File, UploadFile, Request, Response
from fastapi.templating import Jinja2Templates
from logic import NotesDigitizer # Import your class
import uvicorn
import markdown
from xhtml2pdf import pisa
from typing import List
import io

app = FastAPI()
templates = Jinja2Templates(directory="templates")
digitizer = NotesDigitizer()
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/digitize-batch")
async def digitize_batch(files: List[UploadFile] = File(...)):
    file_bytes_list = []
    for file in files:
        content = await file.read()
        file_bytes_list.append(content)

    result_markdown = digitizer.process_batch(file_bytes_list)
    return {"notes": result_markdown}

@app.post("/generate-pdf")
async def generate_pdf(req: PDFRequest):
    pdf_bytes = convert_markdown_to_pdf(req.notes)
    if not pdf_bytes:
        return {"error": "PDF generation failed"}

    return Response(content=pdf_bytes, media_type="application/pdf")
