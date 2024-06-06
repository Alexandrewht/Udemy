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
 diferença - Itens presentes apenas no set da esquer.
 diferença simétrica ^ - Itens que não estão em ambos.
'''

s1 = set('Alexandre')
s2 = set()  # vazio
s3 = {'Alexandre', 1, 2, 3}  # com dados

print(s1)
print(s2)
print(s3)