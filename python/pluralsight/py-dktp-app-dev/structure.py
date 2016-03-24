from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
#app.exec_()
sys.exit(app.exec_()) # exit with an exit code
