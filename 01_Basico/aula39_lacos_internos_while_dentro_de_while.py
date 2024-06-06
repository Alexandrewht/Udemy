'''
 Repetições
 while (enquanto) 
 Executa uma ação enquanto a condição for verdadeira
 Loop infinito -> quando não tem fim
'''
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    
    while coluna <= qtd_colunas:
        coluna += 1
        print(f'{linha=} {coluna=}')
    
    linha += 1
    
print('Acabou.')

'''
 É como se fossem duas engrenagens
 a interna da 5 voltas e a externa da 1 volta
'''