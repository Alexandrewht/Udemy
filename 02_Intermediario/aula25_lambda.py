'''
 Função lambda em Python
 A função lambda é uma função como qualquer
 outra em Python. Porém, são funções anônimas
 que contém apenas uma linha. Ou seja, tudo
 deve ser contido dentro de uma única expressão
 lista = [
     {'nome': 'Alexandre', 'sobrenome': 'white'},
     {'nome': 'Maria', 'sobrenome': 'Luzia'},
     {'nome': 'Valéria', 'sobrenome': 'Cristina'},
     {'nome': 'Leila', 'sobrenome': 'Maria'},
     {'nome': 'Rodolfo', 'sobrenome': 'Cesar'},
     {'nome': 'Paulo', 'sobrenome': 'Henrique'},
 ]
'''

'''lista2 = [3, 32, 1, 34, 5, 6, 6, 21,]
lista3 = [3, 32, 1, 34, 5, 6, 6, 21,]

lista2.sort() # sorted(lista)
lista3.sort(reverse=True)

print(lista2)
print(lista3)'''

lista = [
    {'nome': 'Alexandre', 'sobrenome': 'white'},
    {'nome': 'Maria', 'sobrenome': 'Luzia'},
    {'nome': 'Valéria', 'sobrenome': 'Cristina'},
    {'nome': 'Leila', 'sobrenome': 'Maria'},
    {'nome': 'Rodolfo', 'sobrenome': 'Cesar'},
    {'nome': 'Paulo', 'sobrenome': 'Henrique'},
 ]

def exibir(lista):
    for item in lista:
        print(item)
    print()
#lista.sort(key=ordena) # isso gera um erro.

# usando lambda para colocar uma ordem na lista
#lista.sort(key=lambda item: item['nome'])

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)