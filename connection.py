import os

class Connections:
    def __init__(self, dir):
        self.originDir = dir
        self.extension = {}

    def add_connection(self, extension, destination):
        self.extension[extension] = destination
        


