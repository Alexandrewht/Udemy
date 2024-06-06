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


caminho_arquivo = r'C:\\Dev Python\\Nova pasta Atenção\\'
caminho_arquivo += 'aula 73, 74, 75 e 76.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    
    arquivo.writelines(
        ('Linha 3\n', 'linha 4\n')
    )
    # para ler dentro do arquivo antes de fechar 
    # podemos usar o seek para voltar ao inicio
    arquivo.seek(0, 0)
    print(arquivo.read())
    
    print('lendo')
    
    # readline é similar ao next
    print(arquivo.readline(), end='') 
    print(arquivo.readline().strip()) 
    
    print('READLINES')
    for linha in arquivo.readlines():
        print(linha.strip()) 
