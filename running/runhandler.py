import os
import datetime

from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QAction, QMenu, QDesktopWidget, QFileSystemModel, QListWidgetItem

from ui_files.mainWindow import Ui_MainWindow

from create_archive.createArchive import create
from fileSystem.filehandler import FileHandler


class RunHandler(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.archive_path = None
        self.parent = Ui_MainWindow()
        self.parent.setupUi(self)
        self.createArchive = create(self)
        self.fileHandler = FileHandler(self)

        self.parent.treeWidget.setColumnCount(3)
        self.parent.treeWidget.setColumnWidth(0, 400)
        self.parent.treeWidget.setHeaderLabels(['File/Folder', 'Size', 'Type', 'Modified'])

        self.icon_type = {'folder': ':/icons/icons/folder.svg',
                          'file': ':/icons/icons/empty-page.svg'}


        self.mainLoop()

        # Open Window Center
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def mainLoop(self):
        self.custom_toolBar()
        self.parent.pushButton_add_folder.clicked.connect(self.add_folder_clicked)
        self.parent.pushButton_add_file.clicked.connect(self.add_file_clicked)

        self.model = QFileSystemModel()
        self.model.setRootPath('')

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
        self.parent.pushButton_add_file.setEnabled(True)
        self.parent.pushButton_add_folder.setEnabled(True)

    def add_folder_clicked(self):
        paths = self.fileHandler.select_folders()
        self.write_treeWidget(paths, icon=0)

    def add_file_clicked(self):
        paths = self.fileHandler.select_files()
        self.write_treeWidget(paths, icon=1)

    def write_treeWidget(self, paths, icon):
        # TODO icon_type list
        # 0 = folder
        # 1 = file
        for path in paths:
            item = QtWidgets.QTreeWidgetItem(self.parent.treeWidget)

            #Column = 0 - Dosya
            item.setText(0, self.fileHandler.file_name_modified(path))
            if icon == 0:
                item.setIcon(0, QtGui.QIcon(self.icon_type['folder']))
            if icon == 1:
                item.setIcon(0, QtGui.QIcon(self.icon_type['file']))

            #Column = 1 - Dosya Boyutu
            file_size, unit = self.fileHandler.file_size(path)
            item.setText(1, str(str(round(file_size, 2)) + unit))

            # Column = 2 - Type
            file_type = self.fileHandler.fileType(path)
            item.setText(2, file_type)

            #Column = 3 - Degistirme Tarihi
            last_modified = os.path.getmtime(path)
            date = str(datetime.datetime.fromtimestamp(last_modified))  # '2023-05-01 19:28:07.323678'
            time_value = self.fileHandler.date_modified(date)
            item.setText(3, time_value)