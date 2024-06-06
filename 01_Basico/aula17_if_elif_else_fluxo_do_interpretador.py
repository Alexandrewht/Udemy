# if    /   elif        /   else
# se    /  se não       /   se não

# Quando uma função é checada e verificada como verdadeira
# o bloco vai finalizar por ali e nem vai checar as próximas.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1.1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
    print('Código para condição 3.1')
    print('Código para condição 3.2')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma das condições foram satisfeitas')
    
# Podem ter mais de um if separado por bloco de código, 
# acima faz parte de um, e abaixo é outro

if 10 == 10:
    print('é 10 mesmo')
else:
    ...

if 50 != 50:
    print('50 não é 50')
else:
    print('50 é 50')