import os
import sys
from PyQt5.QtWidgets import QDialog, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from ui_files.createNewArchive import Ui_Form


class create(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.archive_format = None
        self.archive_location = None
        self.archive_name = None
        self.archive_path = None
        self.main_directory = None
        self.create_button_state = False

        self.create_button_state = False

        self.parent = Ui_Form()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.parent.setupUi(self)
        self.parent.archive_name.setFocus(True)
        self.parent.create_button.setEnabled(False)

        # Every time open Create Form in center display
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.close_window()

        # print(self.archive_path)

    def close_window(self):
        self.parent.cancel_button.clicked.connect(lambda: self.close())

    def add_location(self):
        if sys.platform == 'linux':
            self.main_directory = os.path.expanduser('~')
            for index, item in enumerate(os.listdir(self.main_directory)):
                if os.path.isdir(os.path.join(self.main_directory, item)) and not item.startswith('.'):
                    if item[0].isupper():
                        self.parent.comboBox_archive_location.addItem(item)
        self.parent.archive_name.textChanged.connect(self.change_button_state)

    def create_archive_path(self):
        self.archive_name = self.parent.archive_name.text()
        self.archive_location = self.parent.comboBox_archive_location.currentText()
        self.archive_format = self.parent.comboBox_archive_format.currentText()
        # archive_path = self.parent.create_button.clicked.connect(self.connect_path)
        # self.close()
        self.archive_path = os.path.join(self.main_directory, self.archive_location,
                                         self.archive_name + self.archive_format
                                         )
        # if self.archive_path:
        #     self.mainWindow.lineEdit_path.setText(self.archive_path)
        self.close()
        return self.archive_path

    def change_button_state(self):
        if self.parent.archive_name.text() == "":
            self.parent.create_button.setEnabled(False)
        else:
            self.parent.create_button.setEnabled(True)

    def add_item_for_archive(self):
        pass
