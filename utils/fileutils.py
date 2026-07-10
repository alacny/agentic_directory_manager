"""
This module contains tools for manipulating with content of files
"""

# The safe directory is always the current directory. The agent cannot access anything from parent directory

CURRENT_DIR = '.'

from pathlib import Path
from .helperutils import is_path_safe


def read_file(file_name:str) -> str:
    content = ""
    """
    The function reads a line from the file. And returns it.

    """

    if is_path_safe(file_name):

        with open(file_name, "r") as f:
            for line in f:
                content += line

        return content
    else:
        return "The file is outside the current directory!"

if __name__ == "__main__":
    file_to_read = input("Podaj nazwę pliku: ")
    print(read_file(file_to_read), flush = True)
