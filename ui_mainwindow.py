# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(575, 372)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.procesos_label = QLabel(self.centralwidget)
        self.procesos_label.setObjectName(u"procesos_label")
        self.procesos_label.setGeometry(QRect(20, 10, 61, 16))
        self.relojGlobal_label = QLabel(self.centralwidget)
        self.relojGlobal_label.setObjectName(u"relojGlobal_label")
        self.relojGlobal_label.setGeometry(QRect(430, 0, 61, 16))
        self.espera_label = QLabel(self.centralwidget)
        self.espera_label.setObjectName(u"espera_label")
        self.espera_label.setGeometry(QRect(80, 50, 61, 16))
        self.terminados_label = QLabel(self.centralwidget)
        self.terminados_label.setObjectName(u"terminados_label")
        self.terminados_label.setGeometry(QRect(430, 50, 71, 16))
        self.ejecucion_label = QLabel(self.centralwidget)
        self.ejecucion_label.setObjectName(u"ejecucion_label")
        self.ejecucion_label.setGeometry(QRect(260, 110, 61, 16))
        self.lotesPendientes_label = QLabel(self.centralwidget)
        self.lotesPendientes_label.setObjectName(u"lotesPendientes_label")
        self.lotesPendientes_label.setGeometry(QRect(30, 310, 111, 16))
        self.lotesPendientes_label.setScaledContents(False)
        self.enEspera_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.enEspera_plainTextEdit.setObjectName(u"enEspera_plainTextEdit")
        self.enEspera_plainTextEdit.setGeometry(QRect(30, 70, 151, 221))
        self.enEspera_plainTextEdit.setReadOnly(True)
        self.ejecucion_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.ejecucion_plainTextEdit.setObjectName(u"ejecucion_plainTextEdit")
        self.ejecucion_plainTextEdit.setGeometry(QRect(210, 130, 151, 111))
        self.ejecucion_plainTextEdit.setReadOnly(True)
        self.terminados_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.terminados_plainTextEdit.setObjectName(u"terminados_plainTextEdit")
        self.terminados_plainTextEdit.setGeometry(QRect(390, 70, 151, 221))
        self.terminados_plainTextEdit.setReadOnly(True)
        self.numProcesos_lineEdit = QLineEdit(self.centralwidget)
        self.numProcesos_lineEdit.setObjectName(u"numProcesos_lineEdit")
        self.numProcesos_lineEdit.setGeometry(QRect(80, 10, 51, 20))
        self.numProcesos_lineEdit.setInputMethodHints(Qt.ImhNone)
        self.numProcesos_lineEdit.setReadOnly(False)
        self.generar_pushButton = QPushButton(self.centralwidget)
        self.generar_pushButton.setObjectName(u"generar_pushButton")
        self.generar_pushButton.setGeometry(QRect(140, 10, 75, 23))
        self.cont_global_label = QLabel(self.centralwidget)
        self.cont_global_label.setObjectName(u"cont_global_label")
        self.cont_global_label.setGeometry(QRect(500, 0, 47, 13))
        self.cont_lotes_label = QLabel(self.centralwidget)
        self.cont_lotes_label.setObjectName(u"cont_lotes_label")
        self.cont_lotes_label.setGeometry(QRect(150, 310, 47, 13))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 575, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Procesamiento por Lotes", None))
        self.procesos_label.setText(QCoreApplication.translate("MainWindow", u"# Procesos", None))
        self.relojGlobal_label.setText(QCoreApplication.translate("MainWindow", u"Reloj Global: ", None))
        self.espera_label.setText(QCoreApplication.translate("MainWindow", u"EN ESPERA", None))
        self.terminados_label.setText(QCoreApplication.translate("MainWindow", u"TERMINADOS", None))
        self.ejecucion_label.setText(QCoreApplication.translate("MainWindow", u"EJECUCI\u00d3N", None))
        self.lotesPendientes_label.setText(QCoreApplication.translate("MainWindow", u"# de lotes pendientes:", None))
        self.numProcesos_lineEdit.setInputMask("")
        self.generar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.cont_global_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cont_lotes_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

