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

