'''
 Calculo do primeiro dígito do CPF
 CPF: 746.824.890-70
 Colete a soma dos 9 primeiros dígitos do CPF
 multiplicando cada um dos valores por uma
 contagem regressiva começando de 10
 
 Ex.: 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2 
*  7   4  6  8  2  4  8  9  0
   70 36 48 56 12 20  32 27 0
   
   Somar todos os resutaldos:
   70+36+48+56+12+20+32+27+0 = 301
   Multiplicar o resultado anterior por 10
   301*10 = 3010
   Obter o resto da divisão da conta anterior por 11
   3010 % 11 = 7
   Se o resultado anterior for maior que 9:
      resultado é 0
   contrário disso:
      resultado é o valor da conta
'''

# informar o cpf
cpf = input('Digite os 11 primeiros digitos do CPF: ')
while not cpf.isdigit() or len(cpf) != 11:
   cpf = input("CPF inválido. Digite os 11 números do CPF: ")
   
print(f'Você digitou {cpf}')
# coletar os 9 primeiros digitos
digitos_cpf = cpf[:9]
multiplicacao = 10

# digito 1
resultado_digito1 = 0
for digito1 in digitos_cpf:
   resultado_digito1 += (int(digito1) * multiplicacao)
   multiplicacao -= 1
      
digito1 = ((resultado_digito1 * 10) % 11)
digito1 = digito1 if digito1 <= 9 else 0

# digito 2
resultado_digito2 = 0
multiplicacao = 11
cpf_com_digito = digitos_cpf + str(digito1)

for digito2 in cpf_com_digito:
   resultado_digito2 += (int(digito2) * multiplicacao)
   multiplicacao -= 1
      
digito2 = ((resultado_digito2 * 10) % 11)
digito2 = digito2 if digito2 <= 9 else 0

# checagem
cpf_calculado = f'{digitos_cpf}{digito1}{digito2}'

if cpf == cpf_calculado:
   print(f'O {cpf} é válido.')
else:
   print(f'O {cpf} é inválido')

'''RESOLUÇÃO
cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]

contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
   resultado_digito_1 += (int(digito) * contador_regressivo_1)
   contador_regressivo_1 -= 1
digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
   resultado_digito_2 += (int(digito) * contador_regressivo_2)
   contador_regressivo_2 -= 1
digito_2 = ((resultado_digito_2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado_pelo_calculo)

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
   print(f'O {cpf_enviado_usuario} é válido')
else:
   print(f'O {cpf_enviado_usuario} é inválido.')'''
   