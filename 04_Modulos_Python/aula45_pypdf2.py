# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias
# https://pypdf2.readthedocs.io/en/3.0.0/
from pathlib import Path
from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_PDFS = PASTA_RAIZ / 'arquivos_pdfs'

PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos_pdf'
PASTA_NOVA.mkdir(exist_ok=True)

RELATORIO_BACEN = PASTA_PDFS / 'R20230210.pdf'

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]
 
# print(page0.extract_text()) # Retorna o conteúdo da página
# print(len(page0.images)) # Retorna o número de imagens
# print(page0.images[0]) # Retorna dados da imagem

# extraindo imagem de um PDF
with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)