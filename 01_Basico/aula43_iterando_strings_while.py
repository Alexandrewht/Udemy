'''
 Treinamento de algoritimo,
 salvando um valor enquanto executa uma outra tarefa
 depois checa o valor e talvez troque o valor
'''

# barra invertida é para quebrar a linha, 
# tem que abrir a aspas novamente
frase = 'O Python é uma linguagem de programação ' \
    'Multiparadgma.' \
    'Python foi criado por Guido van Rossum.'

# Tem case sensitive, inclusive com acentos 
print(frase.count('Python'))
print(frase.count('python'))
print(frase.count('a'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
        
    i += 1
    
print('A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x'
      )