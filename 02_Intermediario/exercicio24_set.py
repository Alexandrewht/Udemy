'''
 Exercicio
 Crie uma função que encontra o primeiro duplicado
 considerando o segundo número como a duplicação.
 
 Retorne a duplicação considerada.
 
 Requisitos:
    A ordem do número duplicado é considerada a partir
    da segunda ocorrência do número, ou seja, o 
    número duplicado em si.
    Exemplo:
    [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
    [1, 2, 3, 4, 5, 6] -> retorne -1 (não tem duplicados)
    Se não escontrar duplicados na lista, retorne -1
'''

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], #  tem q retorna -1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # tem q retorna 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # tem q retorna 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], # tem q retorna 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], # tem q retorna 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], # tem q retorna 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1], # tem q retorna 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],  # tem q retorna 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],  # tem q retorna 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],  # tem q retorna 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],  # tem q retorna 1
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  # tem q retorna -1
]

# pegando indice e lista
for i, l in enumerate(lista_de_listas_de_inteiros):
    lista_repetidos = [] # lista vazia para armazenar as duplicatas
    conjunto_vistos = set() # conjunto vazio para rastrear os números vistos
    
    for num in l:
        if num in conjunto_vistos:
            lista_repetidos.append(num) # se o número já foi visto, é uma duplicata
        else:
            conjunto_vistos.add(num) # Caso contrário, adicione-o ao conjunto de números vistos
            
    # Verifique se há duplicatas e retorne o resultado
    if lista_repetidos:
        print(f"O primeiro item da lista duplicado é o {lista_repetidos[0]}")
    else:
        print(f"Não tem duplicado: -1")
        
'''# RESOLUÇÃO

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
         
        numeros_checados.add(numero)
        
    return primeiro_duplicado
    
for lista in lista_de_listas_de_inteiros:
    print(
        lista, 
        encontra_primeiro_duplicado(lista))'''
    