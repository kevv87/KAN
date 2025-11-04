import pdfplumber

def process_file(filename:str) -> None:
    pdfplumber.open(filename)
