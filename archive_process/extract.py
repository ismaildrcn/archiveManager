import json
import os
import zipfile
import tarfile
import shutil


class Extract():
    def __init__(self, parent=None):
        self.extract_path = None
        self.finish_write = False
        self.archive_file_list = None
        self._archive_name = None
        self._archive_type = None
        self._archive_path = None
        self.write_data = ''
        self.ops_file_path = os.path.join(os.path.dirname(__file__), '..', 'ops', 'ops_file.ops')

        self._parent = parent

        self.read_operation = {
            'archive_name': None,
            'path': None,
            'archive_type': None,
            'file_size': None,
            'modified_time': None
        }

    def extract_file(self):
        # self._parent.clearQTreeWidget(self._parent.parent.treeWidget)
        self._parent.parent.lineEdit_path.setText(self._archive_path)
        # COMMENT disabled to lineEdit_path edit or write
        self._parent.parent.lineEdit_path.setReadOnly(True)
        if self._archive_type == 'zip':
            self.extract_path = os.path.join(
                os.path.expanduser('~/.archiveManager'),
                self._archive_path.split(os.path.sep)[-1].split('.')[0]
            )
            self.un_zip_files(
                archive_path=self._archive_path,
                extract_path=self.extract_path
            )
            print(self.extract_path)
            self._parent.parent.pushButton_extract.setEnabled(True)

        elif self._parent.operation['archive_type'] == '.tar':
            pass
        elif self._parent.operation['archive_type'] == '.tar.gz':
            pass
        elif self._parent.operation['archive_type'] == '.tar.xz':
            pass
        elif self._parent.operation['archive_type'] == '.tar.bz2':
            pass
        else:
            print("Unidentified Archive Type")
    def move_zip_folder(self):
        target_path = os.path.join(
            f'{os.path.sep}'.join(self._archive_path.split(os.path.sep)[:-1]),
            self._archive_name
        )
        try:
            shutil.move(self.extract_path, target_path)
        except Exception as error:
            print(error)
        self._parent.write_treeView(target_path=target_path)

    def un_zip_files(self, archive_path, extract_path):
        with zipfile.ZipFile(archive_path, 'r') as zipHandler:
            zipHandler.extractall(extract_path)

    def un_tar_files(self):
        pass

    def open_archive_file(self):
        try:
            self._archive_path = self._parent.fileHandler.select_files(mode='open')[0]
            self._archive_type = self._archive_path.split('.')[-1]
            self._archive_name = self._archive_path.split('/')[-1].replace('.' + self._archive_type, '')
            self._parent.parent.pushButton_compress.setVisible(False)
            self._parent.parent.pushButton_extract.setVisible(True)
            self.extract_file()
        except Exception as error:
            print("Open Archive Error: ", error)

    def write_ops_file(self, write_data):
        if not os.path.exists(self.ops_file_path):
            with open(self.ops_file_path, 'w') as ops:
                ops.write(write_data)
        else:
            with open(self.ops_file_path, 'w') as ops:
                ops.write(write_data)
    # time column ayarlanacak değer hatalı runhandler içerisinde bak.
    # tarfile için extract fonksiyonu yazmıştım onun için brachleri kontrol et