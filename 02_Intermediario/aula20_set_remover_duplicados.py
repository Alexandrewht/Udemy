'''
 Sets - Conjuntos em Python (tipo set)
 conjuntos são ensinados na matemática
 https://brasilescola.uol.com.br/matematica/conjunto.htm
 https://escolakids.uol.com.br/matematica/diagrama-de-venn.htm
 Representados graficamente pelo diagrama Venn
 Sets em Python são mutáveis, porém aceitam apenas
 tipos imutáveis como valor interno.
  
 Criando um set
 set(iterável) ou {1, 2, 3}
 
 Sets são eficientes para remover valores duplicados
 de iteráveis
 - eles não tem índices;
 - eles não garantem ordem;
 - eles são iteráveis (for, in, not in)
 
 Métodos úteis:
 add, update, clear, discard
 
 Operações úteis:
 união | união (union) - Une
 intersecção & (intersection) - Itens presentes em ambos
 diferença - Itens presentes apenas no set da esquer
 diferença simétrica ^ - Itens que não estão em ambos
'''

s1 = set() # vazio
s1 = {'Alexandre', 1, 2, 3} # com dados.
print(s1)


s2 = {1, 2, 3, 3, 3, 3, 3, 1} # valores duplicados.
print(s2) 


l1 = [1, 2, 3, 3, 3, 3, 3, 1] # pode ser usado para lista.
s3 = set(l1) # trazendo a lista pro set.
l2 = list(s3) # o set removeu os repetidos.
print(l2) # aqui está a lista sem os repetidos.


s4 = {1, 2, 3, (123,)} # tupla pode ser usada com virgula no final.
print(s4)


# print(s4[1]) # aqui da erro, não é possível buscar por índice.
print(3 not in s4) # bool no set.


for numero in s4: 
    print(numero)