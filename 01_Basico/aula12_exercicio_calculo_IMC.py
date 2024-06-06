"""
Criando um cálculo de IMC básico
"""

nome = 'Alexandre white de mello'
altura = 1.75
peso = 110
imc = peso / (altura * altura)

print(nome, 'tem:', altura, 'de altura,')
print('pesa:', peso, 'quilos e seu IMC é: ')
print(imc)

'''RESOLUÇÃO
nome = 'Alexandre white de mello'
altura = 1.75
peso = 110
imc = peso / altura ** 2

print(nome, 'tem:', altura, 'de altura,')
print('pesa:', peso, 'quilos e seu IMC é: ')
print(imc)
'''