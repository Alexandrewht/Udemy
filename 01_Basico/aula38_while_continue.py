'''
 Repetições
 while (enquanto)
Executa uma ação enquanto a condição for verdadeira
 Loop infinito -> quando não tem fim
'''

contador = 0

while contador <= 100:
    contador += 1 # Se essa linha for comentada, irá entrar em loop infinito.
    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue
    
    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}.')
        continue
    
    print(contador)
    
    if contador == 40:
        break    
    
print('Acabou')