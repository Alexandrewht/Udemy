'''
 DOC: https://docs.python.org/3/library/os.html
 os.path trabalha com caminhos em Windows, Linux e Mac
 os.path é um módulo que fornece funções para trabalhar com caminhos de 
 arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
 entre esses sistemas.
 
 Exemplos do os.path:
 os.path.join: junta strings em um único caminho. Desse modo,
 os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria o caminho
 'pasta1/pasta2/arquivo.txt' no Linux e no mac, e 
 'pasta1\\pasta2\\arquivo.txt' no Windows.
 
 os.path.split: divide um caminho uma tupla (diretório, arquivo).
 Por exemplo, os.path.split: ('home/user/arquivo.txt')
 retornaria ('home/user', 'arquivo.txt').
 
 os.path.exists: retorna True se o caminho especificado existe.
 os.path só trabalha com caminhos de arquivos e não faz nenhuma
 operação de entrada/saída (I/O) com arquivos em si.
'''
import os

#  não está sendo salvado é apenas um demostrativo
caminho = os.path.join('C:\\home\\user', 'Desktop', 'curso', 'arquivo.txt')
print(caminho)

print('-' * 30)
diretorio, arquivo = os.path.split(caminho)
print(diretorio)
print(arquivo)

print('-' * 30)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)  # aqui tráz o arquivo e o caminho

print('-' * 30)
print(os.path.exists(caminho))  # verificar se o caminho existe

# verificar se o caminho dessa aula existe
print(os.path.exists(
    r'C:\Dev\Dev Python\Python na Udemy com Otavio miranda\04'
    r'.Modulos Python (os, datetime, sys, json, csv, selenium,'
    r' pillow e mais))\10.os.py'))

''' OBSERVAÇÃO ADICIONAL:
 Esse 'r' ai você ta dizendo que ta passando a string pra leitura 
 simplificando sem termos técnicos).

 Porque se você digitar normalmente \\ ele vai pensar que é um 'comando' 
 então precisa digitar \\ pra dizer pro programa que você quer digitar \\
 ai quando você usa o 'r' está dizendo que quer passar um diretório, 
 
 Por exemplo, ai ele vai saber que se você digitar \\ é pq quer digitar \\
 qualquer coisa quando eu voltar eu dou uma resposta melhor
 tipo dentro da string vc consegue dar alguns 'comando' tipo , \n, \t, 
 ai se digita só \\ ele pensa que é comando, então vc precisa digitar \\
 pra confirmar pro programa que quer que na string seja \\ e não um comando
 então o r vc ta meio q dizendo "olha eu vou digitar uma string sem comando, 
 quero que fique exatamente do jeito que estou digitando
'''

print('-' * 30)
print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))
