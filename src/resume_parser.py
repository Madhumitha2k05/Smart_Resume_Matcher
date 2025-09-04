# src/resume_parser.py

import docx
import PyPDF2
import os

def read_docx(file_path):
    """Reads text from a .docx file."""
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading docx file {file_path}: {e}")
        return ""

def read_pdf(file_path):
    """Reads text from a .pdf file."""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = []
            for page in pdf_reader.pages:
                full_text.append(page.extract_text())
            return '\n'.join(full_text)
    except Exception as e:
        print(f"Error reading pdf file {file_path}: {e}")
        return ""

def read_resume(file_path):
    """Reads a resume file, supporting .pdf and .docx."""
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.docx':
        return read_docx(file_path)
    elif file_extension == '.pdf':
        return read_pdf(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return ""