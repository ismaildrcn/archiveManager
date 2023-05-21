import os
import zipfile
import tarfile

from running.loghandler import LogHandler, LOGLIST


class Compress():
    def __init__(self, parent=None):
        self._file_list = None
        self._folder_list = None
        self._parent = parent

        self.logHandler = LogHandler(self)
        self.compress_file_list = []

        self._folder_list = []
        self._file_list = []

    def compress_file(self):
        if self._parent.write_operation['archive_type'] == '.zip':
            self.extend_compress_file()
            self.zip_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w'
            )
        elif self._parent.write_operation['archive_type'] == '.tar':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w'
            )
        elif self._parent.write_operation['archive_type'] == '.tar.gz':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w:gz'
            )
        elif self._parent.write_operation['archive_type'] == '.tar.xz':
            self.extend_compress_file()
            self.tar_file(
                path=self._parent.archive_path,
                select_files=self.compress_file_list,
                mode='w:xz'
            )
        elif self._parent.write_operation['archive_type'] == '.tar.bz2':
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
        if self._parent.write_operation['file_folder_list']['folder'] and \
                self._parent.write_operation['file_folder_list']['file']:
            self.compress_file_list.extend(self._parent.write_operation['file_folder_list']['folder'])
            self.compress_file_list.extend(self._parent.write_operation['file_folder_list']['file'])
        elif self._parent.write_operation['file_folder_list']['folder'] and \
                not self._parent.write_operation['file_folder_list']['file']:
            self.compress_file_list.extend(self._parent.write_operation['file_folder_list']['folder'])

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
        try:
            with zipfile.ZipFile(file=path, mode=mode) as zipHandler:
                self.logHandler.log(message=LOGLIST.MESSAGE['1'], parameter1=path)

                # Klasör içindeki tüm dosyaları arşivleme
                for folder in self._folder_list:
                    for folder_path, folder_names, file_names in os.walk(folder):
                        for file in file_names:
                            file_path = os.path.join(folder_path, file)
                            # klasör yapısını koruyarak dosyalar arşive eklendi. 'arcname'
                            arcname = os.path.relpath(file_path, os.path.dirname(folder))  # Klasör içindeki tam konumu koru
                            zipHandler.write(file_path, arcname=arcname)
                            self.logHandler.log(message=LOGLIST.MESSAGE['2'], parameter1=file,
                                                parameter2=path.split(os.path.sep)[-1])

                # dosyaları arşivleme
                for file in self._file_list:
                    zipHandler.write(file, arcname=os.path.basename(file))
            print("All files have been successfully written to the archive.")
            self.logHandler.log(message=LOGLIST.MESSAGE['3'])
        except Exception as error:
            self.logHandler.log(message='An error was caught: ' + error)
            print(error)
        zipHandler.close()

    def tar_file(self, path, select_files, mode):
        self.all_files_added_to_list(select_files)
        try:
            with tarfile.open(path, mode) as tarHandler:
                self.logHandler.log(message=LOGLIST.MESSAGE['1'], parameter1=path)

                for folder in self._folder_list:
                    for folder_path, folder_names, file_names in os.walk(folder):
                        for file in file_names:
                            file_path = os.path.join(folder_path, file)
                            # klasör yapısını koruyarak dosyalar arşive eklendi. 'arcname'
                            arcname = os.path.relpath(file_path, os.path.dirname(folder))  # Klasör içindeki tam konumu koru
                            tarHandler.add(file_path, arcname=arcname)
                            self.logHandler.log(message=LOGLIST.MESSAGE['2'], parameter1=file,
                                                parameter2=path.split(os.path.sep)[-1])

                for file in self._file_list:
                    tarHandler.add(file, arcname=os.path.basename(file))
                print("All files have been written to the archive.")
                self.logHandler.log(message=LOGLIST.MESSAGE['3'])

        except Exception as error:
            self.logHandler.log(message='An error was caught: ' + error)
            print(error)
        tarHandler.close()
