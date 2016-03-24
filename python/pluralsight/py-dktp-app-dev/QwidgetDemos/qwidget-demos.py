from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        line_edit = QLineEdit()
        #line_edit.setText("Hello Pluralsight")
        #line_edit.selectAll()
        #line_edit.setReadOnly(True) # Read-Only Mode
        line_edit.setEchoMode(QLineEdit.Password) # Password
        #text = line_edit.text()
        #print("You typed " + text)     # also print on Python Console

        label = QLabel()
        label.setText("<b>Hello World</b>") # HTML bolded

        self.checkbox = QCheckBox()
        self.checkbox.setText("Check Me!")
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.selected)

        self.combobox = QComboBox()
        #self.combobox.addItem("Item 1")
        #self.combobox.addItem("Item 2")
        #self.combobox.addItem("Item 3")
        self.combobox.addItems(["Item 1", "Item 2", "Item 3"])
        self.combobox.currentIndexChanged.connect(self.selectedForCombo)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(label)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)


        self.setLayout(layout)
        #self.setFocus()


    def selected(self):
        if self.checkbox.isChecked():
            print ("Yay")
        else:
            print ("No")
        pass

    def selectedForCombo(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        print(current_text + " at the index " + current_index)


app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()