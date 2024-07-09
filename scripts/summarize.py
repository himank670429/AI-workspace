from os import path, getcwd, walk
import pickle
from configparser import ConfigParser
import re

class Summarize:
    homepath = None
    @staticmethod
    def Parse():
        try:
            cur_dir = getcwd()
            ignores = ['.workspace/', '.git/']

            config = ConfigParser()
            config.read(path.join(cur_dir, '.workspace/config.cfg'))
            homepath = config['DEFAULT'].get('home')


            with open(path.join(cur_dir, '.workspace\\.workignore'), 'rb') as ignore_file, open(path.join(cur_dir, '.workspace','.files'), 'wb') as file_tree:
                while True:
                    try:
                        ignores.append(pickle.load(ignore_file))
                    except EOFError:
                        break
                
                parsed_files = Summarize.__get_file_names(cur_dir, ignores)
                pickle.dump(parsed_files, file_tree)
                print('File Tree\n================')
                print('\n'.join(parsed_files), '\n\n')
                print('file tree parsed successfully')

        except FileNotFoundError as e:
            print("FileNotFound: workspace not initialized :(")



    def __get_file_names(folder_path, ignores):
        """
        Parses a folder and its subfolders, returning a list of relative file paths.

        Args:
            folder_path: The path to the root folder to be parsed.

        Returns:
            A list containing the relative paths of all files within the folder structure.
        """


        files = []
        prefix_path_len = len(folder_path)
        for root, _, files_in_folder in walk(folder_path):
            relative_path_base = path.relpath(root, folder_path)

            for filename in files_in_folder:
                relative_path = path.join(root, filename)[prefix_path_len+1:]
                    
                if (not Summarize.__should_ignore(ignores, relative_path)):
                    files.append(relative_path)

        return files
    
    def __should_ignore(ignores, file_path):
        """
        Checks if a file should be ignored based on a list of patterns.

        Args:
            ignores: A list of ignore patterns (similar to .gitignore format).
            file_path: The relative path of the file to be checked.

        Returns:
            True if the file should be ignored, False otherwise.
        """
        for ignore_pattern in ignores:
            isFolder = ignore_pattern.endswith('/') or ignore_pattern.startswith("/")
            path_tokens = file_path.split('\\')
            file_name = path_tokens[-1]


            # ignore folder
            if isFolder:
                ignore_pattern = ignore_pattern.replace('/','')
                if ignore_pattern in path_tokens and not ignore_pattern==file_name :
                    return True
            
            elif ignore_pattern.__contains__("*"):
                ignore_pattern = ignore_pattern.replace('*', '.*')
                if (re.search( fr'{ignore_pattern}', fr'{path_tokens[-1]}')):
                    return True
                
            if (file_name==ignore_pattern):
                return True

        return False

    
