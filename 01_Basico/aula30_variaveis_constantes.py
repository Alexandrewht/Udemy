"""
 CONSTANTE = "Variáveis" que não vão mudar 
 variável constante é declarada com letra maiúscula
 Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1

range_do_radar_e_multa = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
    
if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if velocidade_carro_passou_radar_1:
    print('Carro passou radar 1')

if range_do_radar_e_multa and velocidade_carro_passou_radar_1:
    print('O carro foi multado em radar 1')