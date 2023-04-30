from ui_files.mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileSystemModel


class treeView():
    def create_model(self):
        self.model = QFileSystemModel()
        return self.model

    def treeView_widget(self, dir_path):
        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)

        self.parent.treeView.setModel(self.model)
        self.parent.treeView.setRootIndex(self.model.index(dir_path))
        self.parent.treeView.setColumnWidth(0, 250)
        self.parent.label_path.setText(dir_path)