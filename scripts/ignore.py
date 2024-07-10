import pickle
from os import path, getcwd

class Ignore:
    __file_path = '.workspace\\.workignore'
    @staticmethod
    def getAll():
        try:
            with open(path.join(getcwd(), Ignore.__file_path), 'r') as ignore_file:
                file_content = ignore_file.readlines()
                print("".join(file_content))
        except FileNotFoundError as e:
            print("FileNotFound: workspace not initialized :(")
            
    @staticmethod
    def add(arguments):
        try:
            file_content = []
            file_path = path.join(getcwd(), Ignore.__file_path)
            with open(file_path, 'r') as ignore_file:
                file_content = ignore_file.readlines()

            # add new items
            file_content = [i.strip() for i in file_content]
            for i in arguments:
                if i in file_content:
                    continue
                file_content.append(i)

            # add the to file
            with open(file_path, 'w') as ignore_file:
                ignore_file.writelines([f'{i}\n' for i in file_content])

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
                with open(full_path, 'w') as ignore_file:
                    return
            content = []
            with open(full_path, 'r') as ignore_file:
                content = ignore_file.readlines()

            content = [i.strip() for i in content]
            
            result_content = list(set(content) - set(arguments))
            with open(full_path, 'w') as ignore_file:
                ignore_file.writelines([f'{i}\n' for i in result_content])

        except FileNotFoundError as e:
            print("FileNotFound: workspace not initialized :(")       