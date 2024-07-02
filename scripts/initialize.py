from os import path, mkdir, system

class Initialize:

    @staticmethod
    def initial_folder(directory_path):
        folder_name = ".workspace"
        folder_path = path.join(directory_path, folder_name)

        # error handling
        try:
            # create the .workspace folder
            mkdir(folder_path)
            system(f'attrib +h "{folder_path}"') 

            # add ignore file to the .workspace folder
            Initialize.__initialize_ignore(folder_path)

            print(f"initialzed empty workspace in the directory: {folder_path}")

        except OSError as e:
            print(f"Error creating folder: {e}")

    def __initialize_ignore(directory_path):
        file_name = ".workspaceignore"
        try:
            with open(path.join(directory_path, file_name), "wb") as ignore_file: pass
        except OSError as e:
            print(f"Error creating folder: {e}")
        

