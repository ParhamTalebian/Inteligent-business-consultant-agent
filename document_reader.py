# app/document_reader.py
import PyPDF2
import docx

class DocumentReader:
    def __init__(self):
        pass
    
    def read_pdf(self, file_path):
        """
        Reads a PDF file and returns the text.
        """
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text

    def read_docx(self, file_path):
        """
        Reads a DOCX file and returns the text.
        """
        doc = docx.Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    def read_text_file(self, file_path):
        """
        Reads a plain text file and returns the text.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
