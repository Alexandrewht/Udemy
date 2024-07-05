# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1038, 630)
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(2, 0, 1031, 591))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelResult = QLabel(self.gridLayoutWidget)
        self.labelResult.setObjectName(u"labelResult")
        font1 = QFont()
        font1.setPointSize(40)
        self.labelResult.setFont(font1)
        self.labelResult.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelResult, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineName = QLineEdit(self.gridLayoutWidget)
        self.lineName.setObjectName(u"lineName")
        font2 = QFont()
        font2.setPointSize(30)
        self.lineName.setFont(font2)

        self.gridLayout_2.addWidget(self.lineName, 0, 1, 1, 1)

        self.labelName = QLabel(self.gridLayoutWidget)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setFont(font2)

        self.gridLayout_2.addWidget(self.labelName, 0, 0, 1, 1)

        self.buttonSend = QPushButton(self.gridLayoutWidget)
        self.buttonSend.setObjectName(u"buttonSend")
        self.buttonSend.setFont(font2)

        self.gridLayout_2.addWidget(self.buttonSend, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1038, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o tem nada aqui", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Seu nome:", None))
        self.buttonSend.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

