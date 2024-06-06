'''
 Criando arquivos com Python
 
 Usamos a função open para abrir
 um arquivo em Python (ele pode ou não excluir)
 
 Modos:
 r (leitura), w (escrita), x (para criação)
 a (escreve ao final), b (binário)
 t (modo texto), + (leitura e escrita)
 Context manager - with (abre e fecha)
 
 Métodos úteis
 write, read (escrever e ler)
 writelines (escrever várias linhas)
 seek (move o cursor)
 readline (ler linha)
 readlines (ler linhas)
 
 Vamos falar mais sobre o módulo os, mas:
 os.remove ou unlink - apaga o arquivo
 os.rename - troca o nome ou move o arquivo
 
 Vamos falar mais sobre o módulo json, mas:
 json.dump = Gera um arquivo em json
 json.load
'''

import os

caminho_arquivo = r'C:\\Dev Python\\Nova pasta Atenção\\'
caminho_arquivo += 'aula 73, 74, 75 e 76.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    
    arquivo.writelines(
        ('Linha 3\n', 'linha 4\n')
    )
    

#os.unlink(caminho_arquivo)
#os.remove(caminho_arquivo)

# aqui renomeamos (copiamos e criamos um novo arquivo)
# com os mesmos dados
os.rename(caminho_arquivo, 'outro nome.txt')