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

        for p in self.cola_procesos:
            print(p.id)
            print(p.nombre)

    def iniciar(self):
        lote = []
        loteF = []
        ocupado = False
        c_tme = -1

        while True:
            # mostrar lotes pedientes
            pedientes = (math.ceil(len(self.cola_procesos) / self.lote_tam)) - 1
            if (pedientes >= 0):
                self.ui.lotesPendientes_label.setText(f"{pedientes}")

                if not ocupado:
                    for i in range(0, self.lote_tam):
                        lote.append(self.cola_procesos.pop(0))
                    ocupado = True
                # mostrar procesos
                self.mostrarLote(lote, False)
            
                # ejecucion
                if c_tme >= -1:
                    if c_tme == 0 or c_tme >= 0:
                        if c_tme == 0 or c_tme == -1:
                            pcs_exe = lote.pop(0)
                        if pcs_exe.tme == 0:
                            pcs_exe.generarResultado()
                            loteF.append(pcs_exe)
                        
                        if c_tme >= 0:
                            c_tme = pcs_exe.tme
                            self.ui.ejecucion_plainTextEdit.setPlainText(f"{pcs_exe.id}. {pcs_exe.nombre}\n{pcs_exe.operacion}\nTME: {pcs_exe.tme}")
                            pcs_exe.tme -= 1
                        
                    # terminados
                    self.mostrarLote(loteF, True)

                    # reloj global
                    self.ui.cont_global_label.setText(f"{self.reloj_global}")
                    self.reloj_global += 1
                    self.dormicion(1000)
    
    def dormicion(self, time):
        loop = QEventLoop()
        QTimer.singleShot(time, loop.quit)
        loop.exec_()

    def mostrarLote(self, lote, finalizado):
        self.ui.enEspera_plainTextEdit.clear()
        self.ui.terminados_plainTextEdit.clear()
        if not finalizado:
            for p in lote:
                self.ui.enEspera_plainTextEdit.appendPlainText(f"{p.id}. {p.nombre}\n{p.operacion}\nTME: {p.tme}")
        else:
            for p in lote:
                self.ui.terminados_plainTextEdit.appendPlainText(f"{p.id}. {p.nombre}\n{p.operacion}\n = {p.resultado}")
