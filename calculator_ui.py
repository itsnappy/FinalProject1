from PyQt5 import QtCore, QtGui, QtWidgets

class CalculatorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CalculatorApp()
        self.ui.setupUi(self)


class Ui_CalculatorApp(object):
    def setupUi(self, CalculatorApp):
        CalculatorApp.setObjectName("CalculatorApp")
        CalculatorApp.resize(457, 603)
        self.centralwidget = QtWidgets.QWidget(CalculatorApp)
        self.centralwidget.setObjectName("centralwidget")

        #Stating the GUI Buttons
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 10, 411, 91))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget)
        self.percentButton.setGeometry(QtCore.QRect(20, 110, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(20, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(20, 290, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(20, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusminusButton.setGeometry(QtCore.QRect(20, 470, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(130, 470, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(130, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(130, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(130, 110, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(130, 290, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget)
        self.decimalButton.setGeometry(QtCore.QRect(240, 470, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(240, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(240, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(240, 290, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget)
        self.arrowButton.setGeometry(QtCore.QRect(240, 110, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.timesButton = QtWidgets.QPushButton(self.centralwidget)
        self.timesButton.setGeometry(QtCore.QRect(350, 200, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timesButton.setFont(font)
        self.timesButton.setObjectName("timesButton")
        self.subtractButton = QtWidgets.QPushButton(self.centralwidget)
        self.subtractButton.setGeometry(QtCore.QRect(350, 290, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.subtractButton.setFont(font)
        self.subtractButton.setObjectName("subtractButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(350, 380, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(350, 470, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(350, 110, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        CalculatorApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalculatorApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        CalculatorApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalculatorApp)
        self.statusbar.setObjectName("statusbar")
        CalculatorApp.setStatusBar(self.statusbar)

        self.retranslateUi(CalculatorApp)
        QtCore.QMetaObject.connectSlotsByName(CalculatorApp)

        # Connect buttons to functions
        self.connect_buttons()

        # Initialize variables
        self.current_input = ''
        self.current_operator = ''
        self.stored_value = 0

    def connect_buttons(self):
        # Connect buttons to functions
        self.oneButton.clicked.connect(lambda: self.on_digit_button_clicked('1'))
        self.twoButton.clicked.connect(lambda: self.on_digit_button_clicked('2'))
        self.threeButton.clicked.connect(lambda: self.on_digit_button_clicked('3'))
        self.fourButton.clicked.connect(lambda: self.on_digit_button_clicked('4'))
        self.fiveButton.clicked.connect(lambda: self.on_digit_button_clicked('5'))
        self.sixButton.clicked.connect(lambda: self.on_digit_button_clicked('6'))
        self.sevenButton.clicked.connect(lambda: self.on_digit_button_clicked('7'))
        self.eightButton.clicked.connect(lambda: self.on_digit_button_clicked('8'))
        self.nineButton.clicked.connect(lambda: self.on_digit_button_clicked('9'))
        self.zeroButton.clicked.connect(lambda: self.on_digit_button_clicked('0'))

        self.arrowButton.clicked.connect(self.on_arrow_button_clicked)
        self.plusminusButton.clicked.connect(self.on_plusminus_button_clicked)
        self.percentButton.clicked.connect(self.on_percent_button_clicked)
        self.decimalButton.clicked.connect(lambda: self.on_digit_button_clicked('.'))
        self.divideButton.clicked.connect(lambda: self.on_operator_button_clicked('/'))
        self.addButton.clicked.connect(lambda: self.on_operator_button_clicked('+'))
        self.clearButton.clicked.connect(self.on_clear_button_clicked)
        self.timesButton.clicked.connect(lambda: self.on_operator_button_clicked('*'))
        self.subtractButton.clicked.connect(lambda: self.on_operator_button_clicked('-'))
        self.equalButton.clicked.connect(self.on_equal_button_clicked)

    def on_percent_button_clicked(self):
        """Handle percent button click."""
        self.current_input = str(self.stored_value * 0.01)
        self.update_output_label()

    def on_digit_button_clicked(self, digit):
        """Handle digit button click."""
        self.current_input += digit
        self.update_output_label()

    def on_clear_button_clicked(self):
        """Handle clear button click."""
        self.current_input = ''
        self.current_operator = ''
        self.stored_value = 0
        self.update_output_label()

    def on_operator_button_clicked(self, operator):
        """Handle operator button click."""
        if self.current_input:
            if self.current_operator and self.stored_value:
                self.perform_operation()
                self.current_operator = operator  # Update the operator for continuous calculations
            else:
                self.stored_value = float(self.current_input)
                self.current_operator = operator
            self.current_input = ''
            self.update_output_label()

    def on_plusminus_button_clicked(self):
        """Handle plus/minus button click."""
        if self.current_input:
            if self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.update_output_label()

    def on_arrow_button_clicked(self):
        """Handle arrow button click."""
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.update_output_label()

    def on_equal_button_clicked(self):
        """Handle equal button click."""
        if self.current_input and self.current_operator and self.stored_value:
            self.perform_operation()
            self.current_operator = ''  # Reset the operator after completing the operation
            self.current_input = str(self.stored_value)  # Set the current input to the result
            self.update_output_label()

    def perform_operation(self):
        """Perform the arithmetic operation based on the current operator."""
        if self.current_operator == '+':
            self.stored_value += float(self.current_input)
        elif self.current_operator == '-':
            self.stored_value -= float(self.current_input)
        elif self.current_operator == '*':
            self.stored_value *= float(self.current_input)
        elif self.current_operator == '/':
            if float(self.current_input) != 0:
                self.stored_value /= float(self.current_input)
            else:
                self.current_input = ''
                self.current_operator = ''
                self.stored_value = 0
                self.update_output_label()
                # You might want to handle division by zero error here

        self.current_input = ''
        self.update_output_label()
        self.current_operator = ''

    def update_output_label(self):
        """Update the output label with the current input."""
        self.outputLabel.setText(self.current_input or '0')

    def retranslateUi(self, CalculatorApp):
        """Translate UI components."""
        _translate = QtCore.QCoreApplication.translate
        CalculatorApp.setWindowTitle(_translate("CalculatorApp", "Fawaze's Calculator"))
        self.outputLabel.setText(_translate("CalculatorApp", "0"))
        self.percentButton.setText(_translate("CalculatorApp", "%"))
        self.sevenButton.setText(_translate("CalculatorApp", "7"))
        self.fourButton.setText(_translate("CalculatorApp", "4"))
        self.oneButton.setText(_translate("CalculatorApp", "1"))
        self.plusminusButton.setText(_translate("CalculatorApp", "+/-"))
        self.zeroButton.setText(_translate("CalculatorApp", "0"))
        self.eightButton.setText(_translate("CalculatorApp", "8"))
        self.twoButton.setText(_translate("CalculatorApp", "2"))
        self.clearButton.setText(_translate("CalculatorApp", "C"))
        self.fiveButton.setText(_translate("CalculatorApp", "5"))
        self.decimalButton.setText(_translate("CalculatorApp", "."))
        self.threeButton.setText(_translate("CalculatorApp", "3"))
        self.nineButton.setText(_translate("CalculatorApp", "9"))
        self.sixButton.setText(_translate("CalculatorApp", "6"))
        self.arrowButton.setText(_translate("CalculatorApp", "<<"))
        self.timesButton.setText(_translate("CalculatorApp", "x"))
        self.subtractButton.setText(_translate("CalculatorApp", "-"))
        self.addButton.setText(_translate("CalculatorApp", "+"))
        self.equalButton.setText(_translate("CalculatorApp", "="))
        self.divideButton.setText(_translate("CalculatorApp", "/"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    calculator_app = CalculatorApp()
    calculator_app.show()
    sys.exit(app.exec_())
