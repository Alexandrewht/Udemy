'''
 os + shutil - Copiando arquivos com Python
 1 - vamos copiar arquivos de uma pasta para outra.
 
 Mover/Renomear -> shutil.move
 Mover/Renomear -> shutil.rename
 
 Copiar -> shutil.copy
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
os.makedirs(NOVA_PASTA, exist_ok=True)  # cria a pasta se não existir

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        print(caminho_novo_diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_diretorio)
