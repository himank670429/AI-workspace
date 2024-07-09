import click
from os import getcwd

from scripts.initialize import Initialize
from scripts.unintialize import Uninitialize
from scripts.ignore import Ignore
from scripts.summarize import Summarize

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

@click.command()
def parse():
    '''
    generates the summary of the file structure of the currect working directory.
    '''
    Summarize.Parse()




# Ingore commands
@click.command()
@click.argument('arguments', nargs=-1)
def add(arguments):
    '''
    add ignores in .workingore, can pass more than one arguments
    '''
    Ignore.add(arguments)

@click.command()
def listAll():
    '''
    list down all the conent of .workignore
    '''
    Ignore.getAll()

@click.command()
@click.argument('file_path')
def load_from_gitignore(file_path):
    '''
    loading contens from .gitignore into .workignore
    '''
    Ignore.load_from_gitignore(file_path)


@click.command()
@click.argument('arguments', nargs=-1)
@click.option("-a", '--all', is_flag=True, help="use to emtpy out the .workignore")
def remove(arguments, all):
    '''
    removes an item from the .workignore file, can pass more that one argument
    '''
    Ignore.remove(arguments=arguments, all_flag=all)

ignore.add_command(add)
ignore.add_command(remove)
ignore.add_command(listAll, name="list")
ignore.add_command(load_from_gitignore, name="from")


# add all the functions
main.add_command(init)
main.add_command(uninit)
main.add_command(ignore)
main.add_command(parse)

if __name__ == "__main__":
    main()
