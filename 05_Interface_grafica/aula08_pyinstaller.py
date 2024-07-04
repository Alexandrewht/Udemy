# https://pyinstaller.org/en/stable/usage.html#supporting-multiple-python-environments
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/

# tem que entrar no caminho da pasta para fazer a instalação
# no powershell:
# pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='c:\Dev\Udemy\05_Interface_grafica_criando_calculadora\files\;files\' --icon='c:\Dev\Udemy\05_Interface_grafica_criando_calculadora\files\calculadora_icone.jpg' --noconsole --clean --log-level=WARN --distpath="pastaqualquer/dist" --workpath="pastaqualquer/build" --specpath="pastaqualquer/" main.py

''' Anotações sobre o pyinstaller
 Se não estiver o pillow instalado, ele vai dar um erro de nas imagens do programa.
 
 Após fazer a 1° instalação é possível reinstalar o programa, .spec.
 pyinstaller calculadora.spec
 '''