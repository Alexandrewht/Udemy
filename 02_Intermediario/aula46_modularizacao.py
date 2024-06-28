'''
 Modularização - Entendendo os seus próprios módulos Python.
 O primeiro módulo executado chama-se __main__
 Você pode importar outro módulo inteiro ou parte do módulo.
 O python conhece a pasta onde o __main__ está e as pastas
 abaixo dele.
 Ele não reconhece pastas e módulos acima do __main__ por
 padrão.
 O python conhece todos os módulos e pacotes presentes
 nos caminhos de sys.path
'''
try:
    import sys
    sys.path.append('C:\Dev Python\Python na Udemy com Otavio miranda\02.intermediario\package')
    sys.path.append('C:\Dev Python\Python na Udemy com Otavio miranda')
except:
    print('Erro ao importar sys')
    
import modulo_python
import modularizacao_teste

print('Este módulo se chama', __name__)

print()
print(*sys.path, sep='\n')
