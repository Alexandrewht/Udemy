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
 
'''

'''
 o 'w' ele abre o arquivo, apaga tudo
 e escrever de novo oque foi mandado
 
 o 'a' ele não apaga nada e ele começa do final
 
 o 'b' ele vai abrir o arquivo em modo binário
 
 lembrar de sempre usar o arquivo em utf8
'''

caminho_arquivo = r'C:\\Dev Python\\Nova pasta Atenção\\'
caminho_arquivo += 'aula 73, 74, 75 e 76.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    
    arquivo.writelines(
        ('Linha 3\n', 'linha 4\n')
    )
    