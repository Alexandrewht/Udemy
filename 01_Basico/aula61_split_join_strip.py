'''
 split e join com list e str
 split - divide uma string (gera uma lista)
 join - une uma string (une as strings, listas e tuplas)
 strip - corta os espaços do começo e do fim
 rstrip - corta os espaços da direita
 lstrip - corta os espaços da esquerda
'''
frase = 'Olha só que, coisa interessante.'

# split

lista_palavras = frase.split()
lista_frases_cruas = frase.split(', ') # Aqui está pedindo para separar na , e o espaço.

print(lista_palavras)
print(lista_frases_cruas)

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
    
# print(lista_frases_cruas)
# print(lista_frases)

# join

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)