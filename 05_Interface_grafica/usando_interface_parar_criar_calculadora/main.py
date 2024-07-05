import sys
from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)  # Aplica o tema do qdarkstyle
    window = MainWindow()
    window.setWindowTitle('Calculadora')

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)
    
    # Display
    display = Display()
    # display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Botões hardcoded
    # buttonsGrid.addWidget(Button('0'), 0, 0)
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()