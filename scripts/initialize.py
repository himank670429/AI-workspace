from os import path, mkdir, system
import pickle

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

            # add ignore file to the .workspace folder
            Initialize.__inittialize_config(folder_path)

            print(f"initialzed empty workspace in the directory: {folder_path}")

        except OSError as e:
            print(f"Error creating folder: {e}")

    def __initialize_ignore(directory_path):
        file_name = ".workignore"
        try:
            with open(path.join(directory_path, file_name), "wb") as ignore_file: pass
        except OSError as e:
            print(f"Error creating folder: {e}")
    
    def __inittialize_config(directory_path):
        file_name = "config.cfg"
        try:
            with open(path.join(directory_path, file_name), "w") as config_file:
                content = [
                    f'home={directory_path}\n',
                ]
                config_file.writelines(content)
                # pickle.dump(content, config_file)


        except OSError as e:
            print(f"Error creating folder: {e}")
        

