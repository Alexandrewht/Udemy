# QApplication e QPushButton de PySide6.QtWidgets
# QApplication - O widget principal da aplicação
# QPushButton - Botão
# PySide6.QtWidgets -> Onde estão os widget do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv) # Cria uma instância do QApplication

botao = QPushButton('Texto do botão') # Cria um botão
botao.setStyleSheet('font-size: 40px; color: red;')
botao.show() # Adiciona o widget na hierarquia e exibe a janela

app.exec() # Executa o loop da aplicação