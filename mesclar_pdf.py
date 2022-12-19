import os

import PyPDF2

merger = PyPDF2.PdfMerger()



lista_arquivos = os.listdir('data') #ler os arquivos da pasta

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'data/{arquivo}')



merger.write('data/pdf_final.pdf')
print('Procedimento feito com sucesso')

