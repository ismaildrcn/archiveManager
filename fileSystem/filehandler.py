import os
import time
from datetime import datetime
import mimetypes

from fileSystem.filetypelist import FileType
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QListView, QTreeView


class FileHandler(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.extension = None
        self._parent = parent
        self.file_dialog = None
        self.fType = None

        self.fileType = FileType()

    def select_folders(self):
        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        self.file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        file_view = self.file_dialog.findChild(QListView, 'listView')

        # to make it possible to select multiple directories:
        if file_view:
            file_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        f_tree_view = self.file_dialog.findChild(QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        if self.file_dialog.exec():
            paths = self.file_dialog.selectedFiles()
            return paths

    def select_files(self, mode=None):
        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.AnyFile)
        self.file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        if mode == 'open':
            self.file_dialog.setNameFilter("Archive Files (*.zip *.tar *.tar.gz *.tar.xz *.tar.bz2)")
            self.file_dialog.setWindowTitle("Select Archive Files")
        file_view = self.file_dialog.findChild(QListView, 'listView')

        # to make it possible to select multiple directories:
        if file_view:
            file_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        f_tree_view = self.file_dialog.findChild(QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        if self.file_dialog.exec():
            paths = self.file_dialog.selectedFiles()
            return paths

    def file_size(self, path='', mode=True, total=0):
        if mode:
            total = 0
            if os.path.isfile(path):
                total += os.stat(path).st_size
            elif os.path.isdir(path):
                for folder_path, directories, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(folder_path, file)
                        total += os.stat(file_path).st_size
            total_size = len(str(total))
        elif not mode:
            total_size = len(str(total))
        if total_size <= 3:
            return str(total) + ' b'
        elif 3 < total_size <= 6:
            return str(int(total) / 1000) + ' kb'
        elif 6 < total_size <= 9:
            return str(int(total) / 1000000) + ' mb'
        elif 9 < total_size <= 12:
            return str(int(total) / 1000000000) + ' gb'

    def date_modified(self, text, mode=False):
        if not mode:
            text = text.split(' ')
            file_modified_date, file_modified_time = text[0], text[1].split('.')[0]
            date_now, time_now = time.strftime('%Y-%m-%d'), time.strftime('%H:%M:%S')

            if not file_modified_date.split('-')[0] != date_now.split('-')[0] and \
                    file_modified_date.split('-')[1] != date_now.split('-')[1] and \
                    file_modified_date.split('-')[2] != date_now.split('-')[2]:
                return file_modified_date.replace('-', '.')
            else:
                return ':'.join(file_modified_time.split(':')[:2])
        else:
            datetime.strptime(text, )

    def file_name_modified(self, path):
        if os.path.isdir(path):
            file_name = os.sep + path.split(f'{os.sep}')[-1]
        elif os.path.isfile(path):
            file_name = path.split(f'{os.sep}')[-1]
        else:
            file_name = None
        return file_name

    def select_file_type(self, path,  mode=True):
        if not mode:
            self.extension = path[1:].upper()
            if self.extension in self.fileType.fTypes.keys():
                self.fType = self.fileType.fTypes[self.extension]
            else:
                self.fType = 'Undefined'
            return self.fType

        else:
            if os.path.isfile(path):
                self.fType = mimetypes.guess_type(path)[0]
                if self.fType == None:
                    self.fType = 'Undefined'
                print("File Type: ", self.fType)
            elif os.path.isdir(path):
                self.fType = 'Folder'
            else:
                self.fType = 'Undefined'
            return self.fType
