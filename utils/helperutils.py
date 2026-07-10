"""
This module contains tools for manipulating with content of files
"""

# The safe directory is always the current directory. The agent cannot access anything from parent directory
from pathlib import Path
#from functools import wraps
#from typing import Callable, Any

CURRENT_DIR = '.'

# The following might be useful in the future
#
#def armor_path(path_operation: Callable[..., Any]) -> Callable[..., Any]:
#    @wraps(path_operation)
#    def wrapper_function(*args: Any, **kwargs: Any) -> Any:
#        pass


def is_path_safe(file_name:str) -> bool:
    """
    The function check if the file_name is a subdirectory of the current directory
    """
    base_path = Path(CURRENT_DIR)
    resolved_base = base_path.resolve()
    dest_directory = Path(file_name)
    resolved_dest = dest_directory.resolve()
    return resolved_dest.is_relative_to(resolved_base)

    


if __name__ == "__main__":
    pass
