import pickle
from os import path, getcwd
class Ignore:
    __file_path = '.workspace\\.workignore'
    @staticmethod
    def getAll():
        with open(path.join(getcwd(), Ignore.__file_path), 'rb+') as ignore_file:
            while True:
                try:
                    print(pickle.load(ignore_file))
                except EOFError:
                    break

    
    @staticmethod
    def add(arguments):
        with open(path.join(getcwd(), Ignore.__file_path), 'ab') as ignore_file:
            [pickle.dump(f'{i}', ignore_file)for i in arguments]
            
    
    # @TODO: add implementation of this method
    @staticmethod
    def remove(arguments=None, all_flag=False):
        full_path = path.join(getcwd(), Ignore.__file_path)
        # read the content
        if (all_flag):
            with open(full_path, 'wb') as ignore_file:
                return
        content = []
        with open(full_path, 'rb') as ignore_file:
            while True:
                try:
                    content.append(pickle.load(ignore_file))
                except EOFError:
                    break
        
        result_content = list(set(content) - set(arguments))
        with open(full_path, 'wb') as ignore_file:
            [pickle.dump(f'{i}', ignore_file)for i in result_content]
        

        
            