# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0  0.0  ''  False
# Também existe o tipo de None que é
# usado para representar um não valor

# Nessa aula usaremos o or (ou)

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
# # # if True:
# # # ...
senha_permitida = '123'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')    

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)