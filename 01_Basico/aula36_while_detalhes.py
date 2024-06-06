'''
 Repetições
  while (enquanto)
  Executa uma ação enquanto uma condição for verdadeira
  Loop infinito -> Quando um código não tem fim
'''

while False:
    print('EITA') #unreachable, nunca vai ser lido
    
contador = 0

# while contador < 10:
#     contador = contador +1
#     print(contador)
    
while contador <= 10:
    print(contador)
    contador = contador +1
    
print('Acabou')