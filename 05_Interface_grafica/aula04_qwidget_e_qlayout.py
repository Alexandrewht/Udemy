# QWidget e QLayout de PySide6.QtWidgets
# Qwidget - genérico
# Qlayout - é um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv) # Cria uma instância do QApplication

botao = QPushButton('botão 1')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('botão 3')
botao3.setStyleSheet('font-size: 60px;')

central_widget = QWidget() # só serve para ser o pai de outros widgets

# layout = QVBoxLayout()  # Cria um layout na vertical
# layout = QHBoxLayout()  # Cria um layout na horizontal
layout = QGridLayout()  # Cria um layout na vertical
central_widget.setLayout(layout) # Central widget recebe o ultimo layout

layout.addWidget(botao, 1, 1, 1, 1) # coluna, linha, coluna span, linha span
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


central_widget.show() # Central widget entre na hierarquia e exibe a janela
app.exec() # O loop da aplicação
 