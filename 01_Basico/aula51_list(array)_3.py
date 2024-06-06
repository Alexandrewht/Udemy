'''
Conhecimentos reutilizáveis - Índices e fatiamento
 Métodos úteis: 
    append      -> Adiciona um item ao final
    insert      -> Adiciona um item no índice escolhido
    pop         -> Remove do final ou do índice escolhido
    del         -> Apaga um índice
    clear       -> Limpa a lista
    extend      -> Estende a lista
    +           -> Concatena listas
 Create Read Update    Delete -> (CRUD)
 Criar, Ler, Alterar,  Apagar = lista[i] 
'''

#        0    1   2   3
lista = [10, 20, 30, 40]
lista.append('Alexandre')
# nome = lista.pop()
lista.append(1233)
# O índice invertido pode ser utilizado para pegar o ultimo índice
del lista[-1]
print(lista)
# lista.clear() # Clear seria para zerar a lista

# o insert é o único método que recebe 2 argumentos.
lista.insert(0, 'Alexandre')
print(lista)

'''
# Essa parte irá dar erro apenas para fins didáticos.
# IndexError: list index out of range

# Cuidado ao tentar acessar um índice que não existe
print(lista[5]) 

# foi adicionado a string no índice 2000.
lista.insert(2000, 'Alexandre')
print(lista)

# porém não existe índices suficientes.
print(lista[100])
'''