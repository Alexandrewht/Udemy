# https://www.youtube.com/watch?v=1YbTDczvqco

numeros = [1, 2, 3, 4, 5]

novos_numeros = [numero  for numero in numeros]

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

# usando def
def divisaoFN(x, y):
    return x / y

def multiplicacaoFN(x, y):
    return x * y

def potenciacaoFN(x, y):
    return x ** y

print(novos_numeros)
print('------- mapeamento de uma lista em outra -------')
divisao = [divisaoFN(numero, 2) for numero in numeros]
multiplicacao = [divisaoFN(numero, 2) for numero in numeros]

quadrado = [numero ** 2 for numero in numeros]

print(divisao)
print(multiplicacao)
print(quadrado)

print()
print('-------------- filtro --------------')
# filtro, condicionais
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros 
                 if numero > 5]

impares = [numero for numero in numeros
           if numero % 2 != 0]

pares = [numero for numero in numeros
         if numero % 2 == 0]

print(numeros)
print(novos_numeros)
print(impares)
print(pares)

print()
# pegar só os pares e mudar o 6 para 600
outro_if = [numero 
        if numero != 6 else 600
        for numero in pares]

print(outro_if)

print()
print('------- for alinhado (for dentro de for) -------')

for x in range(1, 4): # for pra linhas
    for y in range(1, 4): # for para colunas
        ...
        #print(x, y)
        
# usando o for alinhado em list comprehension
linhas_e_colunas = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 4)
    for y in range(1, 4) # esse for está dentro do outro for
    if x != 2 # pula quando o x = 2
]

print(linhas_e_colunas)

print()
print('-------------- strings --------------')

string = 'Alexandre white'
numero_de_letras = 1
nova_string = '.'.join([string[indice:indice + numero_de_letras] 
                for indice in range(
                0, len(string), numero_de_letras)
               ])

print(nova_string)

print()
print('------- strings dentro de listas -------')

nomes = ['alexandre', 'maria', 'valéria', 'leila']
novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' 
               for nome in nomes]


print(novos_nomes)

print()
print('-------------- flat map --------------')
# lista dentro da lista em varias dimensões
numeros = [[numero, numero ** 2] for numero in range(10)]
print(numeros)

print()
# fazendo a lista flat, sem ter a lista dentro de outra lista
flat = [y 
        for x in numeros
        for y in x 
        ]
print(flat)