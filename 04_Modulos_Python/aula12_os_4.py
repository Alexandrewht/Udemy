'''
 os.walk
 os.walk é uma função que permite percorrer uma estrutura de diretórios de
 maneira recrusiva. Ela gera uma sequência de tuplas, onde cada tupla possui
 três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
 e uma lista de arquivos do diretório atual (files).
'''
import os
from itertools import count

caminho = os.path.join(
    'C:\\Dev\\Dev Python',
    'Python na Udemy com Otavio miranda',
    '04.Modulos Python (os, datetime, sys, json, csv, '
    'selenium, pillow e mais))\\Exemplo_aula11'
)
counter = count()

for root, dirs, files in os.walk(caminho):
    the_conunter = next(counter)
    print(the_conunter, 'ROOT:', root)

    for dir_ in dirs:
        print('  ', the_conunter, 'DIRS:', dir_)

    for file_ in files:
        print('  ', the_conunter, 'FILES:', file_)
        # caminho_completo_arquivo = os.path.join(root, file_)
        # print('  ', the_conunter, 'FILES:', caminho_completo_arquivo)
    print()


# NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
# os.unlink('caminho_completo_arquivo')
