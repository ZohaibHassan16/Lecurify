Lecturify: AI-Powered Notes Organizer
Why I made this
I’m tired of having a camera roll full of blurry, messy photos of my notebook/whiteboard that I can never find again. Lecturify is a tool I built to turn those handwritten lecture notes into actual structured study guides. It reads your handwriting, cleans up the mess, and gives you a readable PDF

What it does
Reads Handwriting: Uses PaddleOCR to scan your photos and turn the scribbles into text.

AI Cleanup: I used the Microsoft Phi-3 model and gave it instructions to act like a "Strict Professor." It takes the raw, messy text and re-organizes it into logical topics and bullet points.

Auto-Merging: If you upload multiple pages, it tries to connect the facts so the notes actually make sense.

PDF Export: Once you're happy with the notes, you can just hit export and get a clean PDF.

The Tech Stuff
OCR: PaddleOCR (for the text extraction).

LLM: Microsoft Phi-3-mini (the "brain" that fixes the formatting).

Backend: FastAPI to handle the image uploads and logic.

Frontend: A basic HTML/JS dashboard so you don't have to run everything through code cells.

How to use it
The Colab way (Easiest)
Upload Lecturify.ipynb to Google Colab.

Run the cells in order.

At the very end, it will give you an ngrok link. Click that to open the dashboard and start uploading your photos!

Running it locally
If you want to run it on your own machine:

Clone this repo.

Install the stuff in requirements.txt.

Run uvicorn main:app --reload in your terminal.

Go to http://127.0.0.1:8000.

Files in this repo
Lecturify.ipynb: The main notebook I used for development.

logic.py: The "engine" that handles the OCR and the AI prompts.

main.py: The server code.

templates/: The HTML/CSS files for the dashboard.