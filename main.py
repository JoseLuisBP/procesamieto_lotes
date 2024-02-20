from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

# Creamos la aplicación
app = QApplication()
# Creamos la ventana y elementos de esta
window = MainWindow()
# Mostramos la ventana
window.show()
# Cierra la aplicación cuando el usuario finalice la app 
sys.exit(app.exec_())
