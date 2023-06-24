import os
import shutil
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
        if self._parent.operation.type == '.zip':
            self.create_zip()
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

    def create_zip(self):
        try:
            with zipfile.ZipFile(
                file=self._parent.operation.save_path,
                mode='w',
                compression=zipfile.ZIP_DEFLATED
            ) as zipHandler:
                self.logHandler.log(message=LOGLIST.MESSAGE['1'], parameter1=self.temp_archive_location)
                for folder, sub_folders, files in os.walk(self.temp_archive_location):
                    for file in files:
                        file_path = os.path.join(folder, file)
                        zipHandler.write(file_path, os.path.relpath(file_path, self.temp_archive_location))
                    for sub_folder in sub_folders:
                        folder_path = os.path.join(folder, sub_folder)
                        zipHandler.write(folder_path, os.path.relpath(folder_path, self.temp_archive_location))
            print("Write Archive")
        #     COMMENT add popup
        except Exception as error:
            print(error)
            self.logHandler.log(message=LOGLIST.ERROR['1'], parameter1=error)

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

    def add_folder_clicked(self):
        paths = self._parent.fileHandler.select_folders()
        if paths:
            self.move_folder_or_files(paths)

    def add_file_clicked(self):
        paths = self._parent.fileHandler.select_files()
        if paths:
            self.move_folder_or_files(paths)

    def move_folder_or_files(self, files):
        if not os.path.exists(self._parent.temp_file_path):
            os.mkdir(self._parent.temp_file_path)

        self.temp_archive_location = os.path.join(
            self._parent.temp_file_path,
            self._parent.operation.name
        )
        if not os.path.exists(self.temp_archive_location):
            os.mkdir(self.temp_archive_location)

        for item in files:
            if os.path.isdir(item):
                destination_folder_path = os.path.join(
                    self.temp_archive_location,
                    item.split(os.path.sep)[-1]
                )
                try:
                    shutil.copytree(
                        item,
                        destination_folder_path
                    )
                except:
                    self._parent.write_treeView(self.temp_archive_location)
            elif os.path.isfile(item):
                destination_file_path = os.path.join(
                    self.temp_archive_location,
                    item.split(os.path.sep)[-1]
                )
                shutil.copy(
                    item,
                    destination_file_path
                )
        self._parent.parent.pushButton_compress.setEnabled(True)

        self._parent.write_treeView(self.temp_archive_location)