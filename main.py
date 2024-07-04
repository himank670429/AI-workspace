import click
from os import getcwd

from scripts.initialize import Initialize
from scripts.unintialize import Uninitialize
from scripts.ignore import Ignore

@click.group
def main():
    ...

@click.group()
def ignore():
    '''
    This function lets you interact with the .workingore file 
    '''
    ...


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


# Ingore commands
@click.command()
@click.argument('arguments', nargs=-1)
def add(arguments):
    Ignore.add(arguments)

@click.command()
def list():
    Ignore.getAll()

@click.command()
@click.argument('arguments', nargs=-1)
@click.option("-a", '--all', is_flag=True, help="remove the entire list from .workignore")
def remove(arguments, all):
    Ignore.remove(arguments=arguments, all_flag=all)

ignore.add_command(add)
ignore.add_command(remove)
ignore.add_command(list)


# add all the functions
main.add_command(init)
main.add_command(uninit)
main.add_command(ignore)

if __name__ == "__main__":
    main()
