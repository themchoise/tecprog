
import os
from pseudogenerator import main as generatepseudo
from py2flowchart import pyfile2flowchart
from pdfgenerator import generator
# assign directory
directory = './ejercicios'
ruta_salida = './pseudoresult/'
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    absolute_path = os.path.abspath(filename)

    archivo_final = ruta_salida + filename +'.txt'

    html_file = f'./flowresult/{filename}.html'
    pdf_result_file =f'./pdfresult/{filename}.pdf'

    html_file_test = f'/flowresult/{filename}.html'
    pdf_result_file_test =f'/pdfresult/{filename}.pdf'
    if os.path.isfile(f):
        generatepseudo(f, archivo_final)
        pyfile2flowchart(f, html_file, {"line-width": 1, "arrow-end": "open"})
