#!/usr/bin/env python3
from pathlib import Path


def create_directory(name_of_directory:str) -> str:
    """Funkcja tworzy katalog o podanej nazwie name_of_directory
    argument: 
        name_of_directory – nazwa katalogu do utworzenia"""
    print("Teraz tworzę Twój katalog")
    name_of_directory = name_of_directory.replace(" ", "_")
    Path(name_of_directory).mkdir(exist_ok = True)
    return f"Katalog {name_of_directory} został utworzony"

def remove_directory(name_of_directory:str) -> str:
    """Funkcja usuwa katalog o podanej nazwie name_of_directory
    argument: 
        name_of_directory – ścieżka do katalogu do usunięcia wraz z nazwą tego katalogu"""
    name_of_directory = name_of_directory.replace(" ", "_")
    Path(name_of_directory).rmdir()
    return f"Katalog {name_of_directory} został usunięty"

def list_content_of_directory(name_of_directory:str = ".") -> str:
    """Funkcja wyświetla zawartość bieżącego katalogu
    argument:
        name_of_directory – nazwa katalogu lub ścieżki do wyświetlenia
    Zwraca: lista nazw katalogów"""
    
    list_of_dirs = [entry.name for entry in Path(name_of_directory).iterdir()]
    return list_of_dirs


# This example demonstrates how to use the Gemini 2.0 Pro model to generate content based on a user query.
def main():
    print(list_content_of_directory(name_of_directory='../Einstein'))
if __name__ == "__main__":
    main()
