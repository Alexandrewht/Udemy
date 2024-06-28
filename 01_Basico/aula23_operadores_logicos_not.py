# Operador lógico 'not'
# Usado para inverter expressões
# not True = False
# not False = True

# o not inverte, o True passa a ser falso, 
# o mesmo vale pro False
print(not True)
print(not False)

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
else:
    print(f'Você escreveu {senha}')