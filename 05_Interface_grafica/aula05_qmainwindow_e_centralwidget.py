# QMainWindow e centralWidget
# -> QApplication (app)
# -> QMainWindow (janela -> setCentralWidget)
#   -> CentralWidget (central_widget)
#       -> Layout (layout)
#           -> Widget 1 (botao1)
#           -> Widget 2 (botao2)
#           -> Widget 3 (botao3)
#   -> show (mostrar a janela)
# -> exec (loop da aplicação)
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QGridLayout

app = QApplication(sys.argv) 
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')


botao = QPushButton('botão 1')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('botão 3')
botao3.setStyleSheet('font-size: 60px;')

layout = QGridLayout() 
central_widget.setLayout(layout) 

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 2, 1, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 1)

def slot_example(statusBar):
    status_bar.showMessage('O slot foi executado.')

    
# statusBar
status_bar = window.statusBar()
status_bar.showMessage('aplicação em execução')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda sb: slot_example(status_bar))


window.show()
app.exec()
 