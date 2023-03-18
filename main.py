from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileSystemModel, QAction, QMenu
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_files.mainWindow import Ui_MainWindow


class winZip(QtWidgets.QMainWindow):
    def __init__(self):
        super(winZip, self).__init__()
        self.parent = Ui_MainWindow()
        self.parent.setupUi(self)
        self.custom_toolBar()
        # self.treeView_widget('/home/ismail')

    def custom_toolBar(self):
        # TODO Menu Action List
        new_archive_action = QAction("New Archive", self)
        open_archive_action = QAction("Open Archive", self)

        # Added menu item after create menu
        menu = QMenu()
        menu.addAction(new_archive_action)
        menu.addSeparator()
        menu.addAction(open_archive_action)

        self.parent.menu_button.setMenu(menu)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = winZip()
    window.show()
    sys.exit(app.exec_())