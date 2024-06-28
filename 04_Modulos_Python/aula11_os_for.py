# os.listdir para navegar em caminhos
import os
'''caminho_usando_rstring = (
    r'C:\\Dev\\Dev Python\\Python na Udemy com Otavio miranda'
    r'\04.Modulos Python (os, datetime, sys, json, csv, selenium, '
    r'pillow e mais))\\Exemplo_aula11'
)'''

caminho = os.path.join(
    'C:\\Dev\\Dev Python',
    'Python na Udemy com Otavio miranda',
    '04.Modulos Python (os, datetime, sys, json, csv, ' 
    'selenium, pillow e mais))\\Exemplo_aula11'
)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagens in os.listdir(caminho_completo_pasta):
        print('  ', imagens)
