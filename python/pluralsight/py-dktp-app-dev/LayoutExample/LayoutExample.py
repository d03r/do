from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class HelloWorld(QDialog):
    def __init__ (self):
        QDialog.__init__(self)
        # super(HelloWorld, self).__init__()

        #layout = QVBoxLayout()
        #layout = QHBoxLayout()
        layout = QGridLayout()

        #label = QLabel("Hello World!")
        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        #layout.addWidget(self.label)
        layout.addWidget(self.label, 0, 0) # Grid Layout are zero-based
        #layout.addWidget(line_edit)
        layout.addWidget(line_edit, 0, 1) # Same row, second column
        #layout.addWidget(button)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        #
        # connect attaches event "clicked" to "self.close"
        # event handler.
        # You should not add () after event handler.

        #line_edit.textChanged.connect(label.setText)
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
sys.exit(app.exec_()) # exit with an exit code
