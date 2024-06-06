# Usando de exemplo o exercício anterior para formatar em f-string
# f significa formatação, existe outra maneria com format
nome = 'Alexandre white de mello'
altura = 1.75
peso = 110
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)