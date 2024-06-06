# importlib

import importlib

import modularizacao_teste

print(modularizacao_teste.variavel)

for i in range(10):
    importlib.reload(modularizacao_teste)
    print(i)

