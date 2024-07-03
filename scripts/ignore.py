import pickle
from os import path, getcwd
class Ignore:
    __file_path = '.workspace\\.workignore'
    @staticmethod
    def getAll():
        ignores = []
        with open(path.join(getcwd(), Ignore.__file_path), 'rb+') as ignore_file:
            while True:
                try:
                    ignores.append(pickle.load(ignore_file))
                except EOFError:
                    break
        if (ignores):
            print(".workignore\n===============")
        for i in ignores:
            print(i)
    
    @staticmethod
    def add(arguments):
        with open(path.join(getcwd(), Ignore.__file_path), 'ab') as ignore_file:
            content = '\n'.join([f'{i}' for i in arguments])
            pickle.dump(content, ignore_file)


    
    # @TODO: add implementation of this method
    @staticmethod
    def remove(arguments):
        with open(path.join(getcwd(), Ignore.__file_path), 'ab') as ignore_file:
            ...