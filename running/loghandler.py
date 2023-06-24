import os
import time


class LOGLIST():
    MESSAGE = {
        '1': "The archive file named '&parameter1' has been created.",
        '2': "The file '&parameter1' has been added to the '&parameter2' archive.",
        '3': "All files have been successfully written to the archive."
    }

    ERROR = {
        '1': "An error occurred while creating the archive: &parameter1"
    }


class LogHandler():
    def __init__(self, parent=None):
        self._parent = parent
        self._mainDir = os.path.expanduser('~')
        self._folder_name = '.archiveManager'
        self._file_name = '.archiveManager.log'

        self.create_folder_or_file()

    def create_folder_or_file(self):
        if not os.path.exists(os.path.join(self._mainDir, self._folder_name)):
            os.mkdir(os.path.join(self._mainDir, self._folder_name))

        if not os.path.exists(os.path.join(self._mainDir, self._folder_name, self._file_name)):
            open(
                file=os.path.join(self._mainDir, self._folder_name, self._file_name),
                mode='w',
                encoding='utf8'
            )

    def log(self, message, parameter1=None, parameter2=None):
        timestamp = time.strftime('%x %r')
        if parameter1:
            message = message.replace('&parameter1', parameter1)
        if parameter2:
            message = message.replace('&parameter2', parameter2)

        line = timestamp + " " + message + '\n'
        with open(os.path.join(self._mainDir, self._folder_name, self._file_name), 'a') as file:
            file.write(line)
