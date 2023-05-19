import os
import zipfile
import tarfile

class Compress():
    def __init__(self, parent=None):
        self._file_list = None
        self._folder_list = None
        self._parent = parent
        self.compress_file_list = []

    def compress_file(self):
        if self._parent.operation['archive_type'] == '.zip':
            if self._parent.operation['file_folder_list']['folder'] and \
                    self._parent.operation['file_folder_list']['file']:
                self.compress_file_list.extend(self._parent.operation['file_folder_list']['folder'])
                self.compress_file_list.extend(self._parent.operation['file_folder_list']['file'])
                self.zipping(
                    path=self._parent.archive_path,
                    select_files=self.compress_file_list,
                    mode='w'
                )
                # with zipfile.ZipFile(file=self._parent.archive_path, mode='w') as zip:
                #     for file in self.compress_file_list:
                #         zip.write(file, arcname=os.path.basename(file))
            elif self._parent.operation['file_folder_list']['folder'] and \
                    not self._parent.operation['file_folder_list']['file']:
                self.compress_file_list.extend(self._parent.operation['file_folder_list']['folder'])

        elif self._parent.operation['archive_type'] == '.rar':
            pass
        elif self._parent.operation['archive_type'] == '.tar':
            pass
        elif self._parent.operation['archive_type'] == '.tar.gz':
            pass
        elif self._parent.operation['archive_type'] == '.tar.xz':
            pass
        else:
            print("Unidentified Archive Type")

    def zipping(self, path, select_files, mode):
        self._folder_list = []
        self._file_list = []
        for file in select_files:
            if os.path.isdir(file):
                self._folder_list.append(file)
            elif os.path.isfile(file):
                self._file_list.append(file)

        with zipfile.ZipFile(file=path, mode=mode) as zip:
            # Klasör içindeki tüm dosyaları arşivleme
            for folder in self._folder_list:
                for folder_path, folder_names, file_names in os.walk(folder):
                    for dosya in file_names:
                        file_path = os.path.join(folder_path, dosya)
                        # klasör yapısını koruyarak dosyalar arşive eklendi. 'arcname'
                        arcname = os.path.relpath(file_path, os.path.dirname(folder))  # Klasör içindeki tam konumu koru
                    zip.write(file_path, arcname=arcname)

            # dosyaları arşivleme
            for file in self._file_list:
                zip.write(file, arcname=os.path.basename(file))
        print("All files have been written to the archive.")

