import pickle
from os import path, getcwd
class Ignore:
    __file_path = '.workspace\\.workignore'
    @staticmethod
    def getAll():
        try:
            with open(path.join(getcwd(), Ignore.__file_path), 'rb+') as ignore_file:
                while True:
                    try:
                        print(pickle.load(ignore_file))
                    except EOFError:
                        break
        except FileNotFoundError as e:
            print("FileNotFound: workspace not initialized :(")
            
    @staticmethod
    def add(arguments):
        try:
            with open(path.join(getcwd(), Ignore.__file_path), 'ab') as ignore_file:
                [pickle.dump(f'{i}', ignore_file)for i in arguments]
        except FileNotFoundError as e:
            print("FileNotFound: workspace not initialized :(")    
    
    @staticmethod
    def load_from_gitignore(gitignore_file_path):
        gitignore_full_path = path.abspath(path.join(getcwd(), gitignore_file_path))
        content = []
        if path.exists(gitignore_full_path):
            with open(gitignore_full_path, 'r') as gitignore:
                content = gitignore.readlines()
                content = filter(lambda x : not x.startswith('#'), content)
                content = [x.strip() for x in content if x.strip()]
            
            Ignore.remove(None, all_flag=True)
            Ignore.add(content)

        else:
            print("could not find .gitignore file :(")
            

    
    @staticmethod
    def remove(arguments=None, all_flag=False):
        try:
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

        except FileNotFoundError as e:
            print("FileNotFound: workspace not initialized :(")

        
            