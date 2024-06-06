'''
 Criando arquivos com Python
 
 Usamos a função open para abrir
 um arquivo em Python (ele pode ou não excluir)
 
 Modos:
 r (leitura), w (escrita), x (para criação)
 a (escreve ao final), b (binário)
 t (modo texto), + (leitura e escrita)
 Context manager - with (abre e fecha)
 
'''


caminho_arquivo = 'C:\\Dev Python\\Nova pasta Atenção\\'
caminho_arquivo += 'aula 73, 74, 75 e 76.txt'

'''arquivo = open(caminho_arquivo, 'w')
#
arquivo.close()'''

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')