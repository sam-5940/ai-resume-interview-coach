from ollama import generate
import pdfplumber

def extract_pdf_text(filepath):

    content = ""

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                content += text + "\n"

    return content.strip()

def resume_anlz(input):
    anlzed_review = generate(model="resume_anlz",prompt=input)
    output = anlzed_review.response.strip()

    return output
    

