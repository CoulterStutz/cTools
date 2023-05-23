import os


class Terminal():
    def __init__(self, current_directory="/"):
        self.current_directory = current_directory

    class DirectoryManager():
        def mkdir(self, filename):
            os.mkdir(filename)

        def rmdir(self, filename):
            os.rmdir(filename)

        def list_files_in_directory(self, directory=None):
            if directory == None:
                os.listdir(self.current_directory)
            else:
                os.listdir(directory)
