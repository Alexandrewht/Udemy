# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias
# https://pypdf2.readthedocs.io/en/3.0.0/
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter 
# pdfwriter pode ser usado para criar arquivos novos

PASTA_RAIZ = Path(__file__).parent
PASTA_PDFS = PASTA_RAIZ / 'arquivos_pdfs'

PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos_pdf'
PASTA_NOVA.mkdir(exist_ok=True)

RELATORIO_BACEN = PASTA_PDFS / 'R20230210.pdf'

reader = PdfReader(RELATORIO_BACEN)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()

    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
