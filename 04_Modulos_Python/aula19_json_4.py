# aula vinda do youtube
# https://www.youtube.com/watch?v=T17BTNKBeJY

# pathlib - https://docs.python.org/3/library/pathlib.html
from pathlib import Path
import shutil

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

ideias = caminho_arquivo.parent / 'ideias'
# print(caminho_arquivo.parent.parent)
# print(caminho_arquivo.parent.parent.parent)
# print(ideias / 'arquivo.txt')

# criando o local do arquivo
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

'''caminho_arquivo.touch()  # criando o caminho_arquivo
# print(caminho_arquivo)
caminho_arquivo.write_text('Olá mundo.')  # salvar o texto no caminho_arquivo
# caminho_arquivo.write_text('Olá de novo.')  # sobrepõe o texto se existir

print(caminho_arquivo.read_text())  # lendo oque tem no caminho_arquivo

caminho_arquivo.unlink()  # deletando o arquivo
'''

''' # salvando várias linhas em um arquivo
    with caminho_arquivo.open('w') as file:
    file.write('Uma linha de texto\n')
    file.write('Outra de texto\n')

print(caminho_arquivo.read_text())'''

# mkdir - significa make dir (fazer um diretório)
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)

subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.json'
outro_arquivo.touch()
outro_arquivo.write_text('{"nome": "Alexandre"}')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('{"nome": "Outro nome"}')
# print(mais_arquivo.read_text())

# deletando a pasta e tudo dentro dela
# caminho_pasta.rmdir()  # vai dar erro, existe um arquivo dentro da pasta

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    # is.file() verifica se é um arquivo
    # is.dir() verifica se é uma pasta
    # exists() verifica se o arquivo existe
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write(f'Olá mundo {i}\n')
        text_file.write(f'file_{i}\n')

# logica para entrar na pasta e sair apagando todos os arquivos
# de forma recursiva
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)