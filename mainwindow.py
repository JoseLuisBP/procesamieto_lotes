from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QEventLoop, QTimer
from ui_mainwindow import Ui_MainWindow
from proceso import Proceso
import math, random

class MainWindow(QMainWindow):
    def __init__(self):
        # Inicializa la clase padre para hacer uso de ella en esta clase hija
        super(MainWindow, self).__init__()
        # Se crea una instancia de la clase donde esta creada la Iterfaz
        # Creado un atributo donde se almacenara y hacer su uso mas facil y rapido
        self.ui = Ui_MainWindow()
        # Inicializa lo necesario para el uso de la interfaz en general
        self.ui.setupUi(self)

        self.cola_procesos = []
        self.reloj_global = 1
        self.lotes_pedientes = 0
        self.lote_tam = 4

        self.ui.generar_pushButton.clicked.connect(self.generar_procesos)


    @Slot()
    def generar_procesos(self):
        numProcesos = int(self.ui.numProcesos_lineEdit.text())

        for i in range(0,numProcesos):
            proceso = Proceso(id=i + 1)
            proceso.generarNombre()
            proceso.generarOperacion()
            proceso.tme = random.randint(3, 11)
            self.cola_procesos.append(proceso)

        self.iniciar()

    def iniciar(self):
        lote = []
        loteF = []

        for i in range(0, self.lote_tam):
            lote.append(self.cola_procesos.pop(0))
        
        prcs_x = lote.pop(0)

        while self.cola_procesos:
            # mostrar lotes pedientes
            pedientes = (math.ceil(len(self.cola_procesos) / self.lote_tam)) - 1
            self.ui.cont_lotes_label.setText(f"{pedientes}")
            
            # en espera
            self.mostrarLote(lote, False)
            # en ejecucion
            if prcs_x.tme <= 0:
                if lote:
                    prcs_x.generarResultado()
                    loteF.append(prcs_x)
                    prcs_x = lote.pop(0)
                else:
                    for i in range(0, self.lote_tam):
                        lote.append(self.cola_procesos.pop(0))
            else:
                self.ui.ejecucion_plainTextEdit.setPlainText(f"{prcs_x.id}. {prcs_x.nombre}\n{prcs_x.operacion}\nTME: {prcs_x.tme}")
                prcs_x.tme -= 1
                # terminados
                self.mostrarLote(loteF, True)
            # reloj global
            self.ui.cont_global_label.setText(f"{self.reloj_global}")
            self.reloj_global += 1
            self.dormicion(1000)

    def dormicion(self, time):
        QTimer.singleShot(time, self.iniciar)  # Llamar a iniciar después del tiempo especificado
        QEventLoop().exec_()

    def mostrarLote(self, lote, finalizado):
        self.ui.enEspera_plainTextEdit.clear()
        self.ui.terminados_plainTextEdit.clear()
        if not finalizado:
            for p in lote:
                self.ui.enEspera_plainTextEdit.appendPlainText(f"{p.id}. {p.nombre}\n{p.operacion}\nTME: {p.tme}")
        else:
            for p in lote:
                self.ui.terminados_plainTextEdit.appendPlainText(f"{p.id}. {p.nombre}\n{p.operacion}\n = {p.resultado}")
