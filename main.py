#!/usr/bin/env python3
from google import genai
from dotenv import load_dotenv
from pathlib import Path

def create_directory(name_of_directory:str) -> str:
    """Funkcja tworzy katalog o podanej nazwie name_of_directory"""
    print("Teraz tworzę Twój katalog")
    name_of_directory = name_of_directory.replace(" ", "_")
    Path(name_of_directory).mkdir(exist_ok = True)
    return f"Katalog {name_of_directory} został utworzony"


# This example demonstrates how to use the Gemini 2.0 Pro model to generate content based on a user query.
def main():
    load_dotenv()
    tools = [create_directory]  # Create a list of tools (functions) that the model can use to generate responses.
    client = genai.Client()

    chat = client.chats.create (
        model="gemma-4-31b-it",  # You can specify the model you want to use here,
        config={
            "tools": tools,  # Pass the tools function to provide the list of countries as a tool for the model to use in generating the response.
        }
    )
    while True:
        name_of_directory = """Zastąp spacje w nazwach podkreśleniami"""
        name_of_directory = input(f"Podaj nazwę katalogu do utworzenia: ")
        response = chat.send_message(f"Stwórz, proszę, katalog o nazwie {name_of_directory}")
        print(response.text)
        finish = input(f"Czy kończymy?")
        if finish == "tak":
            break


if __name__ == "__main__":
    main()
