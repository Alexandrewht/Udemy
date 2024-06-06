'''
 Módulos padrão do Python (import, from, as e *)
 https://docs.python.org/3/py-modindex.html
 inteiro - importe nome_modulo
 Vantagens: você tem o namespace do módulo
 Desvantagens: nomes grandes

 partes - from nome_modulo import objeto1, objeto2
 Vantagens: nomes pequenos
 Desvantagens: sem o nomespace do módulo
 
 alias 1 - import nome_modulo as apelido
 alias 2 - from nome_modulo import objeto as apelido
 Vantagens: você pode reservar nomes para seu código
 Desvantagens: pode ficar fora do padrão da linguagem
 
 má prática - from nome_modulo import *
 Vantagens: importa tudo de um módulo
 Desvantagens: importa tudo de um módulo

'''

''' import normal
import sys

platform = 'A'

print(sys.platform)
print(platform)

sys.exit()
print(123)'''

''' import com nomes reservados
from sys import exit, platform
# Cuidado ao escrever variáveis com o import
#platform = 'A' 

print(platform)
exit()'''

'''colocando apelido no import
import sys as s
sys = 'Alguma coisa'

print(s.platform)
print(sys)'''

'''import com nomes reservador + apelidos
from sys import exit as ex
from sys import platform as pf

print(pf)'''

''' import tudo
# Cuidado ao importar tudo do módulo é arriscado
# sobrescrever com váriaveis

from sys import *

print(platform)
exit()'''