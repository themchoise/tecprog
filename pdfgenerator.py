import pdfkit

def generator(html_file_path,pdf_output_path):
    pdfkit.from_file(html_file_path, pdf_output_path)
