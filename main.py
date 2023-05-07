from PyQt5 import QtWidgets
from running.runhandler import RunHandler


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = RunHandler()
    window.show()
    sys.exit(app.exec_())