import os
import datetime

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMenu, QDesktopWidget, QFileSystemModel

from ui_files.mainWindow import Ui_MainWindow

from create_archive.createArchive import create
from fileSystem.filehandler import FileHandler
from running.compress import Compress
from running.extract import Extract


class RunHandler(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.archive_path = None
        self.clearItem = False
        self.parent = Ui_MainWindow()
        self.parent.setupUi(self)

        self.compress = Compress(self)
        self.extract = Extract(self)
        self.createArchive = create(self)
        self.fileHandler = FileHandler(self)

        self.createArchive.parent.cancel_button.clicked.connect(self.close_create_archive_form)

        self.parent.treeWidget.setColumnCount(3)
        self.parent.treeWidget.setColumnWidth(0, 400)
        self.parent.treeWidget.setHeaderLabels(['File/Folder', 'Size', 'Type', 'Modified'])

        self.icon_type = {'folder': ':/icons/icons/folder.svg',
                          'file': ':/icons/icons/empty-page.svg'}
        self.folder_list = []
        self.file_list = []
        self.write_operation = {
            'base_path': os.path.expanduser('~'),
            'save_path': None,
            'file_folder_list': {
                'folder': [],
                'file': []
            },
            'archive_type': None
            }

        self.parent.lineEdit_path.setTextMargins(0, 0, 0, 0)
        icon = QtGui.QIcon(self.icon_type['folder'])
        self.parent.lineEdit_path.addAction(icon, QtWidgets.QLineEdit.LeadingPosition)
        self.parent.pushButton_compress.setVisible(False)
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
        self.parent.pushButton_compress.clicked.connect(self.compress_clicked)

    def custom_toolBar(self):
        # TODO Menu Action List
        self.menu = QMenu()
        self.new_archive_action = QAction("New Archive", self)
        self.new_archive_action.triggered.connect(self.create_archive_file)
        self.open_archive_action = QAction("Open Archive", self)
        self.open_archive_action.triggered.connect(self.extract.open_archive_file)

        # Added menu item after create menu
        self.menu.addAction(self.new_archive_action)
        self.menu.addSeparator()
        self.menu.addAction(self.open_archive_action)

        self.parent.menu_button.setMenu(self.menu)

    def create_archive_file(self):
        if self.clearItem:
            self.clearQTreeWidget(self.parent.treeWidget)
        self.createArchive.show()
        self.createArchive.add_location()
        self.createArchive.parent.create_button.clicked.connect(self.connect_path)

        # Clicked new_archive_create. changed type to pushButton_compress_extract.
        self.parent.pushButton_compress.setVisible(True)
        self.parent.pushButton_extract.setVisible(False)

        self.clearItem = True

    def close_create_archive_form(self):
        self.parent.pushButton_compress.setVisible(False)
        self.parent.pushButton_extract.setVisible(True)
        self.createArchive.close()

    def connect_path(self):
        self.archive_path = self.createArchive.create_archive_path()
        self.parent.lineEdit_path.setText(self.archive_path)
        self.parent.pushButton_add_file.setEnabled(True)
        self.parent.pushButton_add_folder.setEnabled(True)

    def add_folder_clicked(self):
        paths = self.fileHandler.select_folders()
        if paths:
            self.folder_list.extend(paths)
            self.write_treeWidget(paths, icon=0)

    def add_file_clicked(self):
        paths = self.fileHandler.select_files()
        if paths:
            self.file_list.extend(paths)
            self.write_treeWidget(paths, icon=1)

    def write_treeWidget(self, paths, icon):
        self.parent.pushButton_compress.setEnabled(True)
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

        self.write_operation['save_path'] = self.archive_path
        self.write_operation['archive_type'] = self.createArchive.archive_format

    def open_archive_write_treeWidget(self, file_path):
        parts = file_path.split("/")
        current_item = None

        for part in parts:
            if current_item is None:
                items = self.parent.treeWidget.findItems(part, Qt.MatchExactly | Qt.MatchRecursive)
                if items:
                    current_item = items[0]
                else:
                    current_item = QtWidgets.QTreeWidgetItem(self.parent.treeWidget, [part])
                    current_item.setExpanded(True)
                    if os.path.isdir(os.path.join(*parts[:parts.index(part) + 1])):
                        current_item.setIcon(0, QtGui.QIcon(self.icon_type['folder']))  # Klasör simgesi ayarlayın
                    else:
                        current_item.setIcon(0, QtGui.QIcon(self.icon_type['file']))  # Klasör simgesi ayarlayın

            else:
                items = self.parent.treeWidget.findItems(part, Qt.MatchExactly, 0)
                if items:
                    current_item = items[0]
                else:
                    current_item = QtWidgets.QTreeWidgetItem(current_item, [part])
                    current_item.setExpanded(True)
                    if os.path.isdir(os.path.join(*parts[:parts.index(part) + 1])):
                        current_item.setIcon(0, QtGui.QIcon(self.icon_type['folder']))  # Dosya simgesi ayarlayın
                    else:
                        current_item.setIcon(0, QtGui.QIcon(self.icon_type['file']))  # Dosya simgesi ayarlayın


    def compress_clicked(self):
        self.write_operation['file_folder_list']['folder'] = self.folder_list
        self.write_operation['file_folder_list']['file'] = self.file_list
        self.compress.compress_file()

    def clearQTreeWidget(self, tree):
        # yeni arşiv oluşturmak istendiğinde tüm itemlarım temizlenmesi sağlanır.
        tree.clear()
        self.createArchive.parent.archive_name.clear()
        self.parent.lineEdit_path.clear()
        self.createArchive.parent.comboBox_archive_location.clear()
        self.folder_list = []
        self.file_list = []
        self.parent.pushButton_add_folder.setEnabled(False)
        self.parent.pushButton_add_file.setEnabled(False)
