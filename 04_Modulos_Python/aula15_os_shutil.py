'''
 os + shutil - Apagando arquivos com Python
 CUIDADO: Vamos apagar arquivos.
 
 Mover -> shutil.move
 Renomear -> shutil.rename
 Copiar -> shutil.copy
 Copiar Árvore Recursivamente -> shutil.copytree
 
 Apagar Árvore Recursivamente -> shutil.rmtree
 Apagar arquivos -> os.unlink
 
 CUIDADO AO APAGAR OS DIRETÓRIOS.
'''
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(
    'C:\\Dev\\Dev Python',
    'Python na Udemy com Otavio miranda',
    '04.Modulos Python (os, datetime, sys, json, csv, '
    'selenium, pillow e mais))\\Exemplo_aula11'
)
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

# shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)  # copiando a pasta 
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)  # apagando a pasta
# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')  # renomeando a pasta
