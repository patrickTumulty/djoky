import os
import connection



desktop = "/Users/ptumulty/Desktop"

class FileHandler:

    @staticmethod
    def get_dir_contents(dirPath):
        files = []
        folders = []
        for item in os.listdir(dirPath):
            if os.path.isfile("{}/{}".format(dirPath, item)):
                files.append(item)
            elif os.path.isdir("{}/{}".format(dirPath, item)):
                folders.append(item)
            else:
                pass
        return files, folders

    @staticmethod
    def get_extension(file):
        l = len(file) - 1
        while file[l] != ".":
            l -= 1
            if l < 0:
                return "ERROR"
        return file[l:len(file)]

    @staticmethod
    def move_file(filePath, destination):
        os.system("mv {} {}".format(filePath, destination))


        






