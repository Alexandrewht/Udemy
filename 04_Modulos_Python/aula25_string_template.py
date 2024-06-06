'''
 string.Template para substituir varáveis em textos
 doc: https://docs.python.org/3/library/string.html#template-strings
 Métodos:
 substitute: substitui mas gera erros se faltar chaves
 safe_substitute: substiui sem gerar erros se faltar chaves
 Você também pode trocar o delimitador e outras coisas criando uma subclasse
 de template
'''
import string
import locale
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula25.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='Alexandre',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='A. W. M.',
    telefone='(11) 99999-9999',
)

''' # usando template no Python
texto = """ 
Prezado(a) $nome,

 Informamos que sua mensalidade será cobrada no valor de $valor no dia $data.
 Caso deseje cancelar o serviço, entre em contato com a $empresa pelo
 telefone $telefone.

 Atenciosamente,

 ${empresa},
 Abraços."""

template = string.Template(texto)
print(template.substitute(dados))
# print(template.safe_substitute(dados))'''

class MyTemplate(string.Template):  # Mudando o delimitador
    delimiter = '%'

# usando template no arquivo
with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.substitute(dados))