import os
import sys

from PyQt5.QtWidgets import QDialog, QDesktopWidget
from PyQt5.QtCore import Qt, pyqtSignal

from ui_files.createNewArchive import Ui_Form


class create(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.archive_dir_file_fist = None
        self._parent = parent
        self.archive_format = None
        self.archive_location = None
        self.archive_name = None
        self.archive_path = None
        self.main_directory = None
        self.create_button_state = False
        self.selected_archive_format  = '.zip'

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

        self.parent.archive_name.textChanged.connect(self.handle_text_changed)
        self.parent.comboBox_archive_format.currentIndexChanged.connect(self.handle_text_changed)

    def add_location(self):
        if sys.platform == 'linux':
            self.main_directory = os.path.expanduser('~')
            for index, item in enumerate(os.listdir(self._parent.operation.base_path)):
                if os.path.isdir(os.path.join(self._parent.operation.base_path, item)) and not item.startswith('.'):
                    if item[0].isupper():
                        self.parent.comboBox_archive_location.addItem(item)

        self.archive_dir_file_fist = os.listdir(os.path.join(self._parent.operation.base_path, self.parent.comboBox_archive_location.currentText()))

    def set_archive_detail(self):
        self._parent.operation.location = self.parent.comboBox_archive_location.currentText()
        self._parent.operation.name = self.parent.archive_name.text()
        self._parent.operation.type = self.parent.comboBox_archive_format.currentText()

        self._parent.operation.save_path = os.path.join(
            self._parent.operation.base_path,
            self._parent.operation.location,
            self._parent.operation.name + self._parent.operation.type
        )

        self.close()


    def handle_text_changed(self, text):
        archive_type = False
        self.selected_archive_format = self.parent.comboBox_archive_format.currentText()
        # kayıt lokasyonunda aynı isimde dosya var mı kontrol edilir.
        # varsa labella uyarılır.
        if type(text) == int:
            archive_type = True
            archive_type = self.parent.comboBox_archive_format.currentText()
            text = self.parent.archive_name.text()
        if archive_type and text + archive_type in self.archive_dir_file_fist:
            self.parent.label_warning.setText('A file with that name already exist, Please rename')
            self.parent.create_button.setEnabled(False)
        else:
            self.parent.label_warning.setText('')
            self.parent.create_button.setEnabled(True)


        if text + self.selected_archive_format in self.archive_dir_file_fist:
            self.parent.label_warning.setText('A file with that name already exist, Please rename')
            self.parent.create_button.setEnabled(False)
        else:
            self.parent.label_warning.setText('')
            self.parent.create_button.setEnabled(True)

