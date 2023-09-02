#Import necessary libs
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox
#control 
import sys

#
#initiate a class
class TempConverter(QWidget):
    def __init__(self):
        super().__init__()
  
        self.layout = QVBoxLayout()
    
        self.tempInput = QLineEdit()
        self.unitInput = QComboBox()
        self.unitInput.addItem("C")
        self.unitInput.addItem("F")
        self.resultLabel = QLabel("Result will be shown here")
        self.convertButton = QPushButton("Convert")
        
        self.convertButton.clicked.connect(self.convertTemp)

        self.layout.addWidget(self.tempInput)
        self.layout.addWidget(self.unitInput)
        self.layout.addWidget(self.resultLabel)
        self.layout.addWidget(self.convertButton)

        self.setLayout(self.layout)

    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9

    def convertTemp(self):
        temp = float(self.tempInput.text())
        unit = self.unitInput.currentText()

        if unit == "C":
            result = self.celsius_to_fahrenheit(temp)
            self.resultLabel.setText(f"Temperature in Fahrenheit: {result}")
        elif unit == "F":
            result = self.fahrenheit_to_celsius(temp)
            self.resultLabel.setText(f"Temperature in Celsius: {result}")

app = QApplication(sys.argv)

window = TempConverter()
window.show()

sys.exit(app.exec_())
