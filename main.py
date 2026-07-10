#!/usr/bin/env python3
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv
from pathlib import Path
from utils.dirutils import *
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
        "You are a File Management Agent. Your task is to assist the user "
        "in organizing their directories."
        "Use the appropriate tool depending on the file operation requested by the user."
        "Propose a directory tree where files can be placed by examining their content."
        "After using a tool, inform the user about the operation status."
        "Always answer in the language in which the user request was written."
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
        print("Error!")
    while (user_answer := input(f"What do you want to do? (press \"Q\" if you want to finish) ").strip()).lower() not in ["q"]:
        action_to_perform = user_answer
        try:
            response = chat.send_message(f"{action_to_perform}.")
        except ServerError as e:
            print( f"Error: {e}")

        else:
            print(response.text)
            token_counts(response)



if __name__ == "__main__":
    main()
