from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileSystemModel, QAction, QMenu, QDesktopWidget
from PyQt5.QtCore import pyqtSlot
from ui_files.mainWindow import Ui_MainWindow
from create_archive.createArchive import create


class winZip(QtWidgets.QMainWindow):
    def __init__(self):
        super(winZip, self).__init__()
        self.archive_path = None
        self.parent = Ui_MainWindow()
        self.parent.setupUi(self)
        self.createArchive = create(self)

        self.custom_toolBar()


        # Open Window Center
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def custom_toolBar(self):
        # TODO Menu Action List
        self.menu = QMenu()
        self.new_archive_action = QAction("New Archive", self)
        self.new_archive_action.triggered.connect(self.create_archive_file)
        open_archive_action = QAction("Open Archive", self)

        # Added menu item after create menu
        self.menu.addAction(self.new_archive_action)
        self.menu.addSeparator()
        self.menu.addAction(open_archive_action)

        self.parent.menu_button.setMenu(self.menu)

    def create_archive_file(self):
        self.createArchive.show()
        self.createArchive.add_location()

        self.createArchive.parent.create_button.clicked.connect(self.connect_path)

    def connect_path(self):
        self.archive_path = self.createArchive.create_archive_path()
        self.parent.lineEdit_path.setText(self.archive_path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = winZip()
    window.show()
    sys.exit(app.exec_())