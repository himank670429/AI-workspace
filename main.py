import click
from os import getcwd

from scripts.initialize import Initialize
from scripts.unintialize import Uninitialize

@click.group
def main():
    pass

@click.command()
def init():
    '''
    This function perform the initialization of the workspace folder and generate important stuff
    '''
    # get the folder path
    working_dir = getcwd()

    # initialixe the folder
    Initialize.initial_folder(working_dir)

@click.command()
def uninit():
    '''
    This function uninitializes the workspace folder and deletes the config file to
    '''
    # get the folder path
    working_dir = getcwd()
    
    # uninitialixe the folder
    Uninitialize.uninitialize(working_dir)

# add all the functions
main.add_command(init)
main.add_command(uninit)

if __name__ == "__main__":
    main()
