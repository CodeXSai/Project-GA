import os
from Object.Enum import CONST
class fileio:

    def __init__(self, File_Name):
        self._file_name= File_Name

    def write_file(self,input):
        text_file = open(self._file_name, "a")
        text_file.write(input)
        text_file.close()

    def write_overwrite(self,input):
        text_file = open(self._file_name, "a")
        text_file.write(input)
        text_file.close()

    def file_flush(self):
        open(self._file_name, "w").close()

    def read_file(self):
        return open(self._file_name, 'r')

    def create_folder(self, name, sub_directory):
        if sub_directory is not None:
            directory_list = [self._file_name, sub_directory, CONST.SLASH, name]
            directory = "".join(directory_list)
            if not os.path.exists(directory):
                os.makedirs(directory)
        else:
            directory_list = [self._file_name, "", CONST.SLASH, name]
            directory = "".join(directory_list)
            if not os.path.exists(directory):
                os.makedirs(directory)

        return directory + "\\"

