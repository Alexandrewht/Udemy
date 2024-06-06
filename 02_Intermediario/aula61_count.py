# count é um iteravel e iterator sem fim (itertools)
# o range é um iteravel com fim, mas não é um iterator
from itertools import count

c1 = count(step=10, start=5) # é possível reverter a ordem de start e step.
r1 = range(10, 100, 10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('c1', hasattr(r1, '__iter__'))
print('c1', hasattr(r1, '__next__'))

print()
print('count')
for i in c1:
    if i > 100: # travar o contador em 100
        break 
    
    print(i)
    
print()
print('range')
for i in r1: # o range vai parar na variavel
    if i > 100: 
        break 
    
    print(i)