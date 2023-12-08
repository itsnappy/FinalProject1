from PyQt5 import QtWidgets


class CalculatorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CalculatorApp()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    from calculator_ui import Ui_CalculatorApp

    app = QtWidgets.QApplication(sys.argv)
    calculator_app = CalculatorApp()
    calculator_app.show()
    sys.exit(app.exec_())
