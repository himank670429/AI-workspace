import unittest
from os import walk, path
import re

def should_ignore(ignores : list[str], file_path : str):
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


def get_file_names(folder_path, ignores):
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
                
            if (not should_ignore(ignores, relative_path)):
                files.append(relative_path)

    return files




class testSummarize(unittest.TestCase):
    def test_get_files_names(self):
        self.assertEqual(set(get_file_names('D:\\workspace\\python\\holiday-game-jam',[
            "myenv/",
            "__pycache__/",
            "*.pyc",
            ".workspace/",
            ".git/"
        ])),  {
            ".gitignore",
            "Entity\\Player.py",
            "Entity\\Wall.py",
            "Scene\\GameScene.py",
            "Scene\\MainMenu.py",
            "Scene\\SettingsMenu.py",
            "Story.md",
            "UI\\Button.py",
            "UI\\HealthBar.py",
            "UI\\Text.py",
            "UI\\ToggleButton.py",
            "assets\\level\\level_1.csv",
            "config.py",
            "main.py",
            "Modules\\CSVMapLoader.py",
            "Modules\\Camera.py",
            "Modules\\Map.py",
            "Modules\\Math.py",
            "Modules\\SceneManager.py",
            "requirements.txt",
        })

        self.assertEqual(set(get_file_names("D:\\workspace\\web_devlopment\\web-crwaler\\back-end", [
            'node_modules/',
            '.env',
            '.tmp',
            'logs/',
            '*.log',
            'tmp/',
            'data/',
            '.DS_Store',
            '.vscode',
            '.idea/',
            'npm-debug.log',
            'yarn-error.log',
            'Thumbs.db',
            '.git/'
        ])), {
            ".gitignore",
            "package-lock.json",
            "package.json",
            "src\\controller\\crawl.js",
            "src\\public\\assets\\index-D17Tt2eq.css",
            "src\\public\\assets\\index-XgPkgvdB.js",
            "src\\public\\assets\\instagram-YeqXDqUw.svg",
            "src\\public\\index.html",
            "src\\public\\logo.svg",
            "src\\server.js",
            "src\\utils\\webCrawler.js",
        })



if __name__ == "__main__":
    unittest.main()
    # ignores = [".env", "node_modules/","libs/", "*.json"]
    # result = get_file_names('D:\\workspace\\python\\holiday-game-jam',[
    #         "myenv/",
    #         "__pycache__/",
    #         "*.pyc",
    #         ".workspace/",
    #         ".git/"
    #     ])
    # print('\n'.join(result))