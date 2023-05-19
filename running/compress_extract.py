import os
import zipfile
import tarfile
from rarfile import RarFile


class Compress():
    def __init__(self, parent=None):
        self._file_list = None
        self._folder_list = None
        self._parent = parent
        self.compress_file_list = []

        self._folder_list = []
        self._file_list = []

    def compress_file(self):
        if self._parent.operation['archive_type'] == '.zip':
            self.extend_compress_file()
            self.zip_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w'
            )
        elif self._parent.operation['archive_type'] == '.tar':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w'
            )
        elif self._parent.operation['archive_type'] == '.tar.gz':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w:gz'
            )
        elif self._parent.operation['archive_type'] == '.tar.xz':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w:xz'
            )
        elif self._parent.operation['archive_type'] == '.tar.bz2':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w:bz2'
            )
        else:
            print("Unidentified Archive Type")

    def extend_compress_file(self):
        # dosya ve klasör pathleri tek bir arraye kaydedilir.
        if self._parent.operation['file_folder_list']['folder'] and \
                self._parent.operation['file_folder_list']['file']:
            self.compress_file_list.extend(self._parent.operation['file_folder_list']['folder'])
            self.compress_file_list.extend(self._parent.operation['file_folder_list']['file'])
        elif self._parent.operation['file_folder_list']['folder'] and \
                not self._parent.operation['file_folder_list']['file']:
            self.compress_file_list.extend(self._parent.operation['file_folder_list']['folder'])

    def all_files_added_to_list(self, select_files):
        self._folder_list = []
        self._file_list = []

        for file in select_files:
            if os.path.isdir(file):
                self._folder_list.append(file)
            elif os.path.isfile(file):
                self._file_list.append(file)

    def zip_file(self, path, select_files, mode):
        self.all_files_added_to_list(select_files)

        with zipfile.ZipFile(file=path, mode=mode) as zipHandler:
            # Klasör içindeki tüm dosyaları arşivleme
            for folder in self._folder_list:
                for folder_path, folder_names, file_names in os.walk(folder):
                    for dosya in file_names:
                        file_path = os.path.join(folder_path, dosya)
                        # klasör yapısını koruyarak dosyalar arşive eklendi. 'arcname'
                        arcname = os.path.relpath(file_path, os.path.dirname(folder))  # Klasör içindeki tam konumu koru
                    zipHandler.write(file_path, arcname=arcname)

            # dosyaları arşivleme
            for file in self._file_list:
                zipHandler.write(file, arcname=os.path.basename(file))
        print("All files have been written to the archive.")
        zipHandler.close()

    def tar_file(self, path, select_files, mode):
        self.all_files_added_to_list(select_files)

        with tarfile.open(path, mode) as tarHandler:
            for folder in self._folder_list:
                for folder_path, folder_names, file_names in os.walk(folder):
                    for file in file_names:
                        file_path = os.path.join(folder_path, file)
                        # klasör yapısını koruyarak dosyalar arşive eklendi. 'arcname'
                        arcname = os.path.relpath(file_path, os.path.dirname(folder))  # Klasör içindeki tam konumu koru
                        tarHandler.add(file_path, arcname=arcname)

            for file in self._file_list:
                tarHandler.add(file, arcname=os.path.basename(file))
        print("All files have been written to the archive.")
        tarHandler.close()


class Extract():
    pass
