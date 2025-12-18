# Lecturify: AI-Powered Notes Organizer & Refiner

**Lecturify** is an AI tool designed for students to turn messy, handwritten lecture notes into perfectly structured, searchable study guides. You don't have to scroll through blurry photos of notebooks: Lecturify reads your handwriting, organizes it by topic, and gives you a professional PDF.

## Key Features
* **Handwriting Recognition**: Uses **PaddleOCR** to extract text from your uploaded images.
* **AI Brain**: Powered by **Microsoft Phi-3-mini**, which acts as a "Strict University Professor" to re-organize chaotic notes.
* **Smart Grouping**: Automatically merges related facts from different pages into logical headers.
* **Export to PDF**: Instantly turn your digitized notes into a clean PDF study guide.

## How it Works
1.  **OCR Phase**: The system enhances your images (contrast/sharpness) and extracts every line of text.
2.  **LLM Phase**: The raw text is sent to the Phi-3 model with instructions to fix continuity and format everything into Markdown.
3.  **Web Dashboard**: A simple FastAPI-based interface allows you to upload photos and preview results in real-time.

## Getting Started

### Option 1: Google Colab (Easiest)
1.  Open the `Lecturify.ipynb` file in this repository.
2.  Upload it to [Google Colab](https://colab.research.google.com/).
3.  Run the cells in order. Use the **ngrok** link generated at the end to open your dashboard!

### Option 2: Local Setup (For Developers)
1.  **Clone the repo**:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Lecturify.git](https://github.com/YOUR_USERNAME/Lecturify.git)
    cd Lecturify
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app**:
    ```bash
    uvicorn main:app --reload
    ```
4.  Open `http://127.0.0.1:8000` in your browser.

## Project Structure
* `Lecturify.ipynb`: The original development notebook.
* `logic.py`: The "Engine" containing the OCR and AI logic.
* `main.py`: The FastAPI server handling the web requests.
* `templates/`: Contains the `index.html` file for the user interface.

