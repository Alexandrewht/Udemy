'''
 Sets - Conjuntos em Python (tipo set).
 conjuntos são ensinados na matemática.
 https://brasilescola.uol.com.br/matematica/conjunto.htm
 https://escolakids.uol.com.br/matematica/diagrama-de-venn.htm
 Representados graficamente pelo diagrama Venn.
 Sets em Python são mutáveis, porém aceitam apenas.
 tipos imutáveis como valor interno.
  
 Criando um set
 set(iterável) ou {1, 2, 3}
 
 Sets são eficientes para remover valores duplicados
 de iteráveis.
 - eles não tem índices;
 - eles não garantem ordem;
 - eles são iteráveis (for, in, not in).
 
 Métodos úteis:
 add, update, clear, discard.
 
 Operações úteis:
 união | união (union) - Une.
 intersecção & (intersection) - Itens presentes em ambos.
 diferença - Itens presentes apenas no set da esquerdo.
 diferença simétrica ^ - Itens que não estão em ambos.
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3_union = s1 | s2 # uniu os dois sets removendo os repetidos.
s3_intersection = s1 & s2 # retorna os elementos repetidos.
s3_difference_1 = s1 - s2 # aqui vai mostrar os disponiveis no set1.
s3_difference_2 = s2 - s1 # aqui vai mostrar os disponiveis no set2.
s3_simetric = s1 ^ s2 # retorna os itens que não estão presentes.

print(s3_union)
print(s3_intersection)
print(s3_difference_1)
print(s3_difference_2)
print(s3_simetric)