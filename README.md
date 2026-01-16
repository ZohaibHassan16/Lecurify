# Lecturify

Yo, this is **Lecturify**, a project I built to solve a problem every student has: taking messy unorganized screen captures of white boards during a lecture and trying to make sense of them later.



Lecturify uses **OCR** to read the messy text and an **LLM** to act like a strict professor, restructuring your notes into a clean, logical, connected study guide.



### Features

- **Handwriting to Text:** Uses `PaddleOCR` to scrape text from images of your notes.

- **AI Restructuring:** Uses Microsoft's `Phi-3`  (via HuggingFace) to fix grammar, group related topics, and add headers.

- **PDF Generation:** Instantly converts the cleaned-up Markdown into a downloadable PDF.

- **Web Interface:** A simple, clean UI built with FastAPI and Jinja2 templates.



### Tech Stack

Under the hood:

- **Backend:** Python, FastAPI

- **AI/ML:** `PaddleOCR` (for reading text), `Transformers` + `Phi-3` (for main stuff) and `PyTorch` 

- **Frontend:** HTML/CSS (Jinja2 Templates)

- **Utilities:** `xhtmlpdf2` (PDF Generation), `ngrok` for tunneling



### How to Run This

You will need a GPU if you want to run it locally !! otherwise, Colab is your friend; just open the notebook in colab and run all the cells.



1. **Clone the repo** 

    git clone [http://github.com/ZohaibHassan16/lecturify.git](http://github.com/ZohaibHassan16/lecturify.git)
    cd lecturify

2.  **Install Dependencies**
   
   It's a bit heavy so i recommend using a virtual environment
   
       pip install -r requirements.txt

3. **Run the app**
   
   The code is split into `main.py` (server) and `logic.py` (AI engine)
   
       python main.py

Or if you are using uvicorn directly

    uvicorn main:app --reload

4. **Open it**
   
   Go to `https://localhost:8000` (or whatever localhost it spits out) in your browser.
