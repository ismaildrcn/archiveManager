from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt
import sys
from ui_files.createNewArchive import Ui_Form

class create(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.create_button_status = False
        self.parent = Ui_Form()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.parent.setupUi(self)

        # Every time open Create Form in center display
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.archive()

    def archive(self):
        self.parent.cancel_button.clicked.connect(lambda: self.close())