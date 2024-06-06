# package é uma pasta com arquivos com melhor organização
from sys import path
     
from package.modulo import soma_do_modulo #1
import package.modulo #2
from package import modulo #3

from package.modulo import * #4

# print(*path, sep='\n')

print(soma_do_modulo(5, 6)) #1
print(package.modulo.soma_do_modulo(5, 7)) #2
print(modulo.soma_do_modulo(7, 8)) #3

#4
print(varialvel)
print(soma_do_modulo(3, 2))
print(nova_variavel)