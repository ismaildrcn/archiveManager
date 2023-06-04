import json
import os
import zipfile
import tarfile


class Extract():
    def __init__(self, parent=None):
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
        self._parent.clearQTreeWidget(self._parent.parent.treeWidget)
        if self._archive_type == 'zip':
            self.zip_file()
            print(self.archive_file_list)
            for file_path in self.archive_file_list:
                self._parent.open_archive_write_treeWidget(file_path)
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

    def zip_file(self):
        with zipfile.ZipFile(self._archive_path, 'r') as zipHandler:
            # Zip içerisindeki dosya listesini alın
            self.archive_file_list = zipHandler.namelist()
            for index, item in enumerate(self.archive_file_list):
                info = zipHandler.getinfo(item)
                self.read_operation['path'] = self.archive_file_list[index]
                self.read_operation['archive_name'] = self._archive_name
                self.read_operation['archive_type'] = self._archive_type
                self.read_operation['file_size'] = info.file_size
                date_time = '-'.join([str(item) for item in list(info.date_time)][:3]) + ', ' + \
                            ':'.join([str(item) for item in list(info.date_time)][3:])
                self.read_operation['modified_time'] = date_time

                self.write_data += str(self.read_operation) + '\n'
            self.write_ops_file(self.write_data)
        self.finish_write = True


    def tar_file(self):
        pass

    def open_archive_file(self):
        self._archive_path = self._parent.fileHandler.select_files(mode='open')[0]
        self._archive_type = self._archive_path.split('.')[-1]
        self._archive_name = self._archive_path.split('/')[-1].replace('.' + self._archive_type, '')
        self._parent.parent.pushButton_compress.setVisible(False)
        self._parent.parent.pushButton_extract.setVisible(True)
        self.extract_file()

    def write_ops_file(self, write_data):
        if not os.path.exists(self.ops_file_path):
            with open(self.ops_file_path, 'w') as ops:
                ops.write(write_data)
        else:
            with open(self.ops_file_path, 'w') as ops:
                ops.write(write_data)
