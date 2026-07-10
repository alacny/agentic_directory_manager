#!/usr/bin/env python3
from pathlib import Path
from .helperutils import is_path_safe


def create_directory(name_of_directory:str) -> str:
    """Creates directory name_of_directory
    argument: 
        name_of_directory – the name of the directory to be created"""
    if is_path_safe(name_of_directory):
        print("I'm creating your directory")
        name_of_directory = name_of_directory.replace(" ", "_")
        Path(name_of_directory).mkdir(exist_ok = True)
        return f"The directory {name_of_directory} has been created"
    else:
        return f"The directory {name_of_directory} is outside the current directory!"

def remove_directory(name_of_directory:str) -> str:
    """Removes the directory name_of_directory
    argument: 
        name_of_directory – path to the directory to be removed"""
    if is_path_safe(name_of_directory):
        name_of_directory = name_of_directory.replace(" ", "_")
        Path(name_of_directory).rmdir()
        return f"Directory {name_of_directory} has been removed"
    else:
        return f"Directory {name_of_directory} is outside the current directory and hasn't been removed!"


def list_content_of_directory(name_of_directory:str = ".") -> str:
    """Lists the content of the directory name_of_directory
    argument:
        name_of_directory – path to the directory the content of to be listed
    returns: list of the directories"""

    if is_path_safe(name_of_directory):
    
        list_of_dirs = [entry.name for entry in Path(name_of_directory).iterdir()]
        return list_of_dirs
    else:
        return f"Directory {name_of_directory} is outside the current directory!"



# This example demonstrates how to use the Gemini 2.0 Pro model to generate content based on a user query.
def main():
    print(create_directory(name_of_directory='../Einstein'))
    print(list_content_of_directory(name_of_directory='../Einstein'))
    print(remove_directory(name_of_directory='../Einstein'))
if __name__ == "__main__":
    main()
