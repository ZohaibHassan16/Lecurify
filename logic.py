import torch
from paddleocr import PaddleOCR
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from PIL import Image, ImageEnhance
import numpy as np
import io
import warnings
import sys
import subprocess
import gc

# Memory Cleanup
if 'digitizer' in locals(): del digitizer
gc.collect()
torch.cuda.empty_cache()

warnings.filterwarnings("ignore")

# CUDA Check
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Using device: {device}")

class NotesDigitizer:
    def __init__(self):
        print("⏳ Loading OCR...")
        self.ocr_engine = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

        print("⏳ Loading LLM ...")
        model_id = "microsoft/Phi-3-mini-4k-instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            trust_remote_code=True,
            device_map="auto",
            attn_implementation="eager"
        )

        self.llm_pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=2500,
            do_sample=True,
            temperature=0.1
        )
        print("✅ Systems Online.")

    def preprocess_image(self, image_bytes):
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.8)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)
        return np.array(img)

    def process_batch(self, image_files_bytes):
        """Process multiple images, extract text with OCR, and structure with LLM."""
        clean_pages = []
        total_pages = len(image_files_bytes)
        print(f"📚 Processing {total_pages} pages individually...")

        # OCR Phase
        for idx, img_bytes in enumerate(image_files_bytes):
            try:
                enhanced_image = self.preprocess_image(img_bytes)
                result = self.ocr_engine.ocr(enhanced_image, cls=True)
                page_text_lines = []
                if result and result[0]:
                    for line in result[0]:
                        text = line[1][0]
                        if "_____" in text:
                            continue
                        page_text_lines.append(text)

                # Format this page's text
                raw_text = "\n".join(page_text_lines)
                clean_pages.append(f"--- PAGE {idx+1} ---\n{raw_text}")
                print(f"   ✓ Page {idx+1} processed successfully")

            except Exception as e:
                print(f"   ✗ Error on Page {idx+1}: {str(e)[:100]}...")
                clean_pages.append(f"--- PAGE {idx+1} (FAILED) ---\n[OCR Error: {str(e)[:50]}...]")

        # Combine all pages for LLM processing
        full_context = "\n\n".join(clean_pages)

        # LLM Phase
        print("🧠 Structuring notes with LLM...")

        prompt = f"""<|user|>
You are a strict University Professor. You have been given a student's unordered, chaotic lecture notes.
Your task is to RESTRUCTURE them into a perfect study guide.

Here is the chaotic raw text from multiple pages:
{full_context}

RULES FOR RESTRUCTURING:
1. **Ignore Page Order**: Group facts by TOPIC, not by page number. If Page 1 and Page 8 discuss the same concept, merge them.
2. **Create Logical Headers**: Use # Main Topic and ## Subtopic.
3. **Fix Continuity**: If a sentence cuts off on one page and resumes on another, merge it.
4. **Format**: Use Markdown. Use bullet points for lists. Use code blocks for code.

Output the final study guide now.
<|end|>
<|assistant|>"""

        try:
            output = self.llm_pipe(
                prompt,
                max_new_tokens=2500,
                temperature=0.3,
                do_sample=True
            )

            final_notes = output[0]['generated_text']


            if "<|assistant|>" in final_notes:
                final_notes = final_notes.split("<|assistant|>")[1].strip()

            print("✅ Notes structured successfully!")
            return final_notes

        except Exception as e:
            print(f"⚠️ LLM error: {e}")
            # Fallback
            return f"""# Recovery Mode - Raw OCR Text

The LLM failed to structure the notes. Here is the raw extracted text:

{full_context}

*Note: This is unprocessed OCR output. It may contain errors and lacks structure.*"""

# Instantiating
digitizer = NotesDigitizer()