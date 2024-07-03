# é recomendado ativar o ambiente virtual, por que a biblioteca PySide6 é grande.
# pip install pyside6 # tem aproximadamente 210mb de download.
# doc: https://doc.qt.io/qtforpython/
import PySide6.QtCore

print(PySide6.__version__) # imprime a versão do PySide6

print(PySide6.QtCore.__version__) # imprime a versão do Qt compilada no PySide6