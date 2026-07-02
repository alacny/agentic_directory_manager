#!/usr/bin/env python3
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv
from pathlib import Path
from utils.dirtools import *

# This example demonstrates how to use the Gemini 2.0 Pro model to generate content based on a user query.
def main():
    load_dotenv()
    tools = [create_directory,
             remove_directory,
             list_content_of_directory,]  # Create a list of tools (functions) that the model can use to generate responses.
    sys_instr = ( 
        "Jesteś Agentem Zarządzania Plikami. Twoim zadaniem jest pomaganie użytkownikowi "
        "w organizacji jego katalogów."
        "Używaj odpowiedniego narzędzia w zależności od tego, o jaką operację plikową poprosi Cię użytkownik."
        "Jeżeli pierwszym znakiem w  nazwie katalogu lub pliku jest kropka, zignoruj tę nazwę i jedynie wyświetl informację o jej istnieniu."
        "Po użyciu narzędzia, poinformuj "
        "użytkownika o statusie operacji."
    )
    client = genai.Client()
    try:

        chat = client.chats.create (
            model="gemma-4-31b-it",  # You can specify the model you want to use here,
            config={
                "tools": tools,  # Pass the tools function to provide the list of countries as a tool for the model to use in generating the response.
                "system_instruction": sys_instr,
            }
    )
    except:
        print("Nastąpił błąd!")
    while (user_answer := input(f"Co mam zrobić? (Gdybyś chciał skończyć, napisz: \"kończymy\") ").strip()).lower() not in ["kończymy"]:
        action_to_perform = user_answer
        try:
            response = chat.send_message(f"{action_to_perform}.")
        except ServerError as e:
            print( f"Wystąpił błąd: {e}")

        else:
            print(response.text)


if __name__ == "__main__":
    main()
