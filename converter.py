import pdfplumber
import pyttsx3

def convert_pdf_to_audio(pdf_path, output_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text:
            return "No text found in the PDF."

        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()

        return f"Audiobook saved to {output_path}"
    except Exception as e:
        return f"Error: {e}"