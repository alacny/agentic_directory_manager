#!/usr/bin/env python3
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv
from pathlib import Path
from utils.dirtools import *
from utils.fileutils import *
from utils.stats import token_counts

# This example demonstrates how to use the Gemini 2.0 Pro model to generate content based on a user query.
def main():
    load_dotenv()
    tools = [create_directory,
             remove_directory,
             list_content_of_directory,
             read_file,]  # Create a list of tools (functions) that the model can use to generate responses.
    sys_instr = ( 
        "Jesteś Agentem Zarządzania Plikami. Twoim zadaniem jest pomaganie użytkownikowi "
        "w organizacji jego katalogów."
        "Używaj odpowiedniego narzędzia w zależności od tego, o jaką operację plikową poprosi Cię użytkownik."
        "Proponuj drzewo katalogów, w których pliki można umieścić, badając ich zawartość."
        "Jeżeli podana przez użytkownika nazwa katalogu lub pliku ma znak kropki '.'  na początku, zignoruj tę nazwę i jedynie wyświetl informację,"
        "że nie możesz operować na nazwach zaczynających się od kropki."
        "Nie wolno Ci też operować na żadnych danych w katalogu nadrzędnym w stosunku do bieżącego. Jeżeli użytkownik Cię, o to poprosi, odmów grzecznie, ale zdecydowanie."
        "Po użyciu narzędzia, poinformuj użytkownika o statusie operacji."
    )
    client = genai.Client()
    try:

        chat = client.chats.create (
            model="gemma-4-31b-it",  # You can specify the model you want to use here,
#            model="gemini-2.5-flash",  # You can specify the model you want to use here,
#            model="gemini-2.5-flash-lite",  # You can specify the model you want to use here,
            config={
                "tools": tools,  # Pass the tools function to provide the list of countries as a tool for the model to use in generating the response.
                "system_instruction": sys_instr,
            }
    )
    except:
        print("Nastąpił błąd!")
    while (user_answer := input(f"Co mam zrobić? (Gdybyś chciał skończyć, naciśnij literkę \"Q\") ").strip()).lower() not in ["q"]:
        action_to_perform = user_answer
        try:
            response = chat.send_message(f"{action_to_perform}.")
        except ServerError as e:
            print( f"Wystąpił błąd: {e}")

        else:
            print(response.text)
            token_counts(response)



if __name__ == "__main__":
    main()
