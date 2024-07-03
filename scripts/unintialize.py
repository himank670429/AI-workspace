from os import path, rmdir, listdir, remove

class Uninitialize:
    @staticmethod
    def uninitialize(directory_path):
        folder_name = ".workspace"
        folder_path = path.join(directory_path, folder_name)
        try:
            if (path.exists(folder_path)):
                rmdir(folder_path)
                print(f"Uninitialized workspace from the directory : {folder_path}")
            else:
                print(f"Cannot uninitialize workspace from the directory : {folder_path}, workspace folder not found :(")
        # folder not empty
        except OSError as e:
            Uninitialize.__delete_files(directory_path)
            rmdir(folder_path)
            print(f"Uninitialized workspace from the directory : {folder_path}")
    
    def __delete_files(directory_path):
        for content in listdir(directory_path):
            content_path = path.join(directory_path, content)
            if (path.isdir(content_path)):
                Uninitialize.__delete_files(content_path)
            else:
                remove(content_path)
        
