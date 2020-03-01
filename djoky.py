

import os
from file_methods import FileHandler as fh
from connection import Connections

def main():
    app = Djoky()
    app.txt_line_parse()
    app.clean()


class Djoky:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.connection_dict = {}

    def read_path_list(self):
        with open("pathConnections.txt", 'r') as fin:
            lines = [item.strip() for item in fin.readlines()]
        while '' in lines : lines.remove('')
        for item in lines:
            if item[0] == "#":
                lines.remove(item)
        return lines
                
    def txt_line_parse(self):
        lines = self.read_path_list()
        for item in lines:
            obj = item.split("->")
            orig = self.home_dir + obj[0].strip()[3:]
            ext = obj[1].strip()
            dest = self.home_dir + obj[2].strip()[3:]
            if self.connection_dict.get(orig): 
                self.connection_dict[orig].add_connection(ext, dest)
            else:
                newConnection = Connections(orig)
                newConnection.add_connection(ext, dest)
                self.connection_dict[orig] = newConnection

    def clean(self):
        state = False
        for key in self.connection_dict.keys():
            files, folders = fh.get_dir_contents(key)
            conObj = self.connection_dict.get(key)
            for f in files:
                if conObj.extension.get(fh.get_extension(f)):
                    state = True
                    destination = conObj.extension.get(fh.get_extension(f))
                    if os.path.exists(destination) == False:
                        os.system("mkdir {}".format(destination))
                        print("Creating... {}".format(destination))
                    print("Moving {} to {}".format(f, destination))
                    fh.move_file("'{}/{}'".format(conObj.originDir, f), "'{}'".format(destination))
        if state == False:
            print("\nNo Files Moved")
        else:
            print("DONE!")

if __name__ == "__main__":
    main()

