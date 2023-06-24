import os
import pathlib
import shutil

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QAction, QMenu, QDesktopWidget, QMessageBox, QPushButton
from datetime import datetime
from ui_files.mainWindow import Ui_MainWindow

from create_archive.createArchive import create
from create_archive.operation import Operation
from fileSystem.filehandler import FileHandler
from archive_process.compress import Compress
from archive_process.extract import Extract
from running.popup import Popup


class RunHandler(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model_treeView = None
        self.drag_and_drop_activate = False
        self.ops_data = []
        self.ops_file_path = os.path.join(os.path.dirname(__file__), '..', 'ops', 'ops_file.ops')
        self.temp_file_path = os.path.join(os.path.expanduser('~/.archiveManager'), 'temp')
        self.parent = Ui_MainWindow()
        self.parent.setupUi(self)

        self.compress = Compress(self)
        self.extract = Extract(self)
        self.createArchive = create(self)
        self.operation = Operation()
        self.fileHandler = FileHandler(self)
        self.popup = Popup(self)

        self.createArchive.parent.cancel_button.clicked.connect(self.close_create_archive_form)

        self.icon_type = {'folder': ':/icons/icons/folder.svg',
                          'file': ':/icons/icons/empty-page.svg'}
        self.folder_list = []
        self.file_list = []

        self.parent.lineEdit_path.setTextMargins(0, 0, 0, 0)
        icon = QtGui.QIcon(self.icon_type['folder'])
        self.parent.lineEdit_path.addAction(icon, QtWidgets.QLineEdit.LeadingPosition)
        self.parent.pushButton_compress.setVisible(False)
        self.parent.widget_drag_and_drop.setVisible(False)

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
        self.parent.pushButton_add_folder.clicked.connect(self.compress.add_folder_clicked)
        self.parent.pushButton_add_file.clicked.connect(self.compress.add_file_clicked)

        self.parent.pushButton_compress.clicked.connect(self.compress.compress_file)
        self.parent.pushButton_extract.clicked.connect(self.extract.move_zip_folder)

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
        # self.clearQTreeWidget(self.parent.treeView)
        self.createArchive.show()
        self.createArchive.add_location()
        self.createArchive.parent.create_button.clicked.connect(self.connect_path)

        # Clicked new_archive_create. changed type to pushButton_compress_extract.
        self.parent.pushButton_compress.setVisible(True)
        self.parent.pushButton_extract.setVisible(False)

    def close_create_archive_form(self):
        self.parent.pushButton_compress.setVisible(False)
        self.parent.pushButton_extract.setVisible(True)
        self.createArchive.close()

    def connect_path(self):
        self.createArchive.set_archive_detail()
        self.parent.widget_drag_and_drop.setVisible(True)
        self.drag_and_drop_activate = True
        self.setAcceptDrops(True)
        # COMMENT enabled to lineEdit_path edit or write
        self.parent.lineEdit_path.setText(self.operation.save_path)
        self.parent.lineEdit_path.setReadOnly(False)
        self.parent.pushButton_add_file.setEnabled(True)
        self.parent.pushButton_add_folder.setEnabled(True)

    def write_treeView(self, target_path=None):
        # Klasör yapısını göstermek için bir QFileSystemModel oluştur
        self.model_treeView = QStandardItemModel()
        self.model_treeView.setHorizontalHeaderLabels(['Name', 'Size', 'Type', 'Modified'])

        self.parent.treeView.setModel(self.model_treeView)

        self.populate_tree(target_path, self.model_treeView.invisibleRootItem())

        # Sütun genişliklerini ayarla
        self.parent.treeView.setColumnWidth(0, 300)
        self.parent.treeView.setColumnWidth(1, 100)
        self.parent.treeView.setColumnWidth(2, 200)
        self.parent.treeView.setColumnWidth(3, 180)

    def populate_tree(self, folder_path, parent_item):
        for item_name in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item_name)
            item = QStandardItem(item_name)

            if os.path.isdir(item_path):
                item.setIcon(QtGui.QIcon(self.icon_type['folder']))
                self.populate_tree(item_path, item)
                parent_item.appendRow(item)
            else:
                item.setIcon(QtGui.QIcon(self.icon_type['file']))

                size_item = QStandardItem(str(self.fileHandler.file_size(mode=False, total=str(os.path.getsize(item_path)))))
                type_item = QStandardItem(str(self.fileHandler.select_file_type(os.path.splitext(item_name)[1], mode=False)))
                modified_item = QStandardItem(
                    str(datetime.fromtimestamp(
                        pathlib.Path(item_path).stat().st_mtime
                    )).split('.')[0]
                )

                parent_item.appendRow([item, size_item, type_item, modified_item])

    def read_ops_file(self):
        if os.path.exists(self.ops_file_path):
            with open(self.ops_file_path, 'r') as ops:
                self.ops_data = ops.readlines()

            self.ops_data = [item.replace('\n', '') for item in self.ops_data]

    def clearQTreeWidget(self, tree):
        # yeni arşiv oluşturmak istendiğinde tüm itemlarım temizlenmesi sağlanır.
        self.createArchive.parent.archive_name.clear()
        self.parent.lineEdit_path.clear()
        self.createArchive.parent.comboBox_archive_location.clear()
        self.parent.pushButton_add_folder.setEnabled(False)
        self.parent.pushButton_add_file.setEnabled(False)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if self.drag_and_drop_activate:
            self.parent.pushButton_compress.setEnabled(True)
            if event.mimeData().hasUrls():
                drop_urls = [url.toLocalFile() for url in event.mimeData().urls()]
                self.compress.move_folder_or_files(drop_urls)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if os.path.exists(self.temp_file_path):
            shutil.rmtree(self.temp_file_path)
        else:
            pass