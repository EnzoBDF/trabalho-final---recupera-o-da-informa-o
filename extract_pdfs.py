import os
from PyPDF2 import PdfReader

PASTA_PDFS = 'data/pdfs'
SAIDA = 'data/documents.txt'

def extrair_texto_pdf(caminho_pdf):
    reader = PdfReader(caminho_pdf)
    texto = ''
    for page in reader.pages:
        texto += page.extract_text() or ''
    return texto.replace('\n', ' ').strip()

os.makedirs('data', exist_ok=True)
with open(SAIDA, 'w', encoding='utf-8') as fout:
    for nome_arquivo in os.listdir(PASTA_PDFS):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho = os.path.join(PASTA_PDFS, nome_arquivo)
            texto = extrair_texto_pdf(caminho)
            if texto:
                fout.write(f'{nome_arquivo}\t{texto}\n') 