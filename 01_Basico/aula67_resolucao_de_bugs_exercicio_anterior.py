'''
 Solução de alguns possíveis bugs
 O normal é utulizar pontos, traços entre outros
 74682489070 = 746.824.890-70
'''
import re # (Regular Expression) expressão regular
import sys # importar dados do systema

# Pode- se usar o replace para remover ou trocar por outro
'''cpf_enviado_usuario = '746.824.890-70' \
   .replace('.', '') \
   .replace(' ', '') \
   .replace('-', '') 
'''
entrada = input('CPF [746.824.890-70]:')
cpf_enviado_usuario = re.sub(
   r'[^0-9]', # Tudo que não é um número é substituido
   '', # foi substituido para nada
   # assim é possível remover todos caracteres
   entrada)  

# checagem de repetição
entrada_e_sequendial = entrada == entrada[0] *len(entrada)

# Aqui se o usuário digitar letras sequênciais, já fecharia o programa
if entrada_e_sequendial:
   print('Vocên enviou dados sequênciais')
   sys.exit()
''' checagem para não permitir caracteres repetidos
primeiro_caractere_entrada = entrada[0]
primeiro_caractere_entrada_repetido = \
   primeiro_caractere_entrada * len(entrada)
print(entrada, primeiro_caractere_entrada_repetido)'''
   

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
#print(cpf_gerado_pelo_calculo)

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
   print(f'O {cpf_enviado_usuario} é válido')
else:
   print(f'O {cpf_enviado_usuario} é inválido.')