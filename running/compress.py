import os
import shutil
import zipfile
import tarfile

from running.loghandler import LogHandler, LOGLIST


class Compress():
    def __init__(self, parent=None):
        self.temp_archive_location = None
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

        elif self._parent.operation.type == '.tar':
            self.create_tar(mode='w')

        elif self._parent.operation.type == '.tar.gz':
            self.create_tar(mode='w:gz')

        elif self._parent.operation.type == '.tar.xz':
            self.create_tar(mode='w:xz')

        elif self._parent.operation.type == '.tar.bz2':
            self.create_tar(mode='w:bz2')
        else:
            print("Unidentified Archive Type")

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
                        arc_name = os.path.relpath(file_path, self.temp_archive_location)
                        zipHandler.write(file_path, arcname=arc_name)
                    for sub_folder in sub_folders:
                        folder_path = os.path.join(folder, sub_folder)
                        arc_name = os.path.relpath(folder_path, self.temp_archive_location)
                        zipHandler.write(folder_path, arcname=arc_name)
            print("Write Archive")
            zipHandler.close()
            # COMMENT add popup
        except Exception as error:
            print(error)
            self.logHandler.log(message=LOGLIST.ERROR['1'], parameter1=error)
            zipHandler.close()

    def create_tar(self, mode):
        try:
            with tarfile.open(
                name=self._parent.operation.save_path,
                mode=mode
            ) as tarHandler:
                self.logHandler.log(message=LOGLIST.MESSAGE['1'], parameter1=self.temp_archive_location)
                for folder, sub_folders, files in os.walk(self.temp_archive_location):
                    for file in files:
                        file_path = os.path.join(folder, file)
                        arc_name = os.path.relpath(file_path, self.temp_archive_location)
                        tarHandler.add(file_path, arcname=arc_name)
                        self.logHandler.log(message=LOGLIST.MESSAGE['2'], parameter1=file,
                                            parameter2=self.temp_archive_location.split(os.path.sep)[-1])
                    for sub_folder in sub_folders:
                        folder_path = os.path.join(folder, sub_folder)
                        arc_name = os.path.relpath(folder_path, self.temp_archive_location)
                        tarHandler.add(folder_path, arcname=arc_name)
                        # COMMENT The processed sub folder is removed from the list so that it is not rewritten.
                        sub_folders.remove(sub_folder)
            tarHandler.close()
        except Exception as error:
            print(error)
            self.logHandler.log(message=LOGLIST.ERROR['1'], parameter1=error)
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