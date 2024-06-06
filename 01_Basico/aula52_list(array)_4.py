'''
 Listas em Python
 Suporta vários valores de qualquer tipo
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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

# o extend usou o método para a lista A
lista_d = lista_a.extend(lista_b)

print(lista_d)
print(lista_a)