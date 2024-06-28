# + Web Scraping com Python usando requests e bs4 (BeautifulSoup)
# - Web Scraping é o ato de "raspas a web" buscando informações de forma
#   automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é o responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - DOC: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

# https://docs.python.org/3/howto/unicode.html  # Documentação do unicode

import requests
from bs4 import BeautifulSoup
import re

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
print(top_jobs_heading.text)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    # print(article)

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{2,}', '', p.text).strip())