'''
 Faça um jogo para o usuário adivinhar qual palavra secreta.
 
 - Você vai propor uma palavra secreta qualquer e vai dar
 a possíbilidade para o usuário digitar apenas uma letra.
 
 - Quando o usuário digitar uma letra, você vai conferir se
 a letra digitada está na palavra secreta.
   Se a letra digitada estiver na palavra secreta; 
 exiba a letra.
   Se a letra digitada não estiver na palavra secreta; 
 exiba *.
 
 - Faça uma contagem de tentativas do seu usuário.
'''

# escrever palavra secreta. (concluido)
# usuario digitar uma letra. (concluido)
# verificar erros ao digitar uma letra. (concluido)
# transformar palavra secreta em *. (concluido)
# se acertar tirar o * e colocar a letra. (concluido)
# fazer contagem de tentativas. (concluido)

palavra_secreta = 'perfume'
letra_adivinhada = '*' * len(palavra_secreta)
tentativas = 0

print("Tente adivinhar a palavra secreta.")
while '*' in letra_adivinhada:
  print(f'Palavra atual = {letra_adivinhada}')
  
  letra_digitada = input('Digite uma letra: ')
  qtd_letra = len(letra_digitada) 
    
  if qtd_letra > 1:
    print('Você precisa digitar apenas uma letra.')
  elif letra_digitada.isdigit():
    print('A palavra secreta não contém números.')
  
  if letra_digitada in palavra_secreta:
    nova_letra = ''
    for i in range(len(palavra_secreta)):
      if palavra_secreta[i] == letra_digitada:
        nova_letra += letra_digitada
      else:
        nova_letra += letra_adivinhada[i]
    letra_adivinhada = nova_letra
  else:
    print('letra não encontrada na palavra secreta.')
    
  tentativas += 1
  
print(f'Parabéns você conseguiu! a palavra secreta era "{palavra_secreta}".')
print('Número de tentativas:', tentativas)
  
''' RESOLUÇÃO
# limpando após ser concluido
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:  
  letra_digitada = input('Digite uma letra: ')
  numero_tentativas += 1
  
  if len(letra_digitada) > 1:
    print('Digite apenas uma letra.')
    continue
  
  if letra_digitada in palavra_secreta:
    letras_acertadas += letra_digitada
  
  palavra_formada = ''
  
  for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
      palavra_formada += letra_secreta
    else:
      palavra_formada += '*'
  
  print('Palavra formada:', palavra_formada)
      
  if palavra_formada == palavra_secreta:
    os.system('cls')
    print('VOCÊ GANHOU!! PARABÉNS!')
    print('A palavra secreta era ', palavra_secreta)
    print('Tentativas: ', numero_tentativas)
    letras_acertadas = ''
    numero_tentativas = 0
'''