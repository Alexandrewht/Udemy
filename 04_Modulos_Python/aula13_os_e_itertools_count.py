# os.pathgetsize e os.stat para dados dos arquivos
import os
import math
from itertools import count

caminho = os.path.join(
    r'C:\\Dev\\Dev Python\\Python na Udemy com Otavio miranda'
    r'\04.Modulos Python (os, datetime, sys, json, csv, selenium, '
    r'pillow e mais))\\Exemplo_aula11'
)


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"

    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1024 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos

    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia

    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


'''print(formata_tamanho(1_000))
print(formata_tamanho(1_000_000))
print(formata_tamanho(1_000_000_000))
print(formata_tamanho(1_000_000_000_000))
print(formata_tamanho(1_000_000_000_000_000))'''


counter = count()

for root, dirs, files in os.walk(caminho):
    the_conunter = next(counter)
    print(the_conunter, 'ROOT:', root)

    for dir_ in dirs:
        print('  ', the_conunter, 'DIRS:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        
        # esse código tem a mesma funcionalidade do de baixo
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        
        print('  ', the_conunter, 'FILES:', file_, formata_tamanho(tamanho))
    print()
