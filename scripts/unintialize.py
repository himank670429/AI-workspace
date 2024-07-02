from os import path, rmdir

class Uninitialize:
    @staticmethod
    def uninitialize(directory_path):
        folder_name = ".workspace"
        folder_path = path.join(directory_path, folder_name)

        if (path.exists(folder_path)):
            rmdir(folder_path)
            print(f"Uninitialized workspace from the directory : {folder_path}")
        else:
            print(f"Cannot uninitialize workspace from the directory : {folder_path}, workspace folder not found :(")
