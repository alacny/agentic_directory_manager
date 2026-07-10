#!/usr/bin/env python3
#!/usr/bin/env python3
from typing import Any, Callable, List
from google import genai
from google.genai import types
from google.genai.errors import APIError
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Twoje prawdziwe importy - jawne i bezpieczne
from utils.dirutils import create_directory, remove_directory, list_content_of_directory
from utils.fileutils import read_file
from utils.stats import token_counts

class FileAgent:
    """
    Synchronous File Management Agent.
    Clean, tested structure adapted for synchronous utils functions.
    """
    def __init__(
        self,
        model_name: str = "gemini-2.5-flash",
        tools: List[Callable[..., Any]] | None = None,
        system_instruction: str | None = None
    ) -> None:
        load_dotenv()
        self.client: genai.Client = genai.Client()
        self.model_name: str = model_name
        self.tools: List[Callable[..., Any]] = tools or []
        self.system_instruction: str = system_instruction or "You are a helpful assistant."
        self.chat: Any = None

    def initialize_session(self) -> None:
        """Initializes the synchronous chat session with the model."""
        config = types.GenerateContentConfig(
            tools=self.tools,
            system_instruction=self.system_instruction,
            temperature=0.2,
        )
        # Używamy standardowego, synchronicznego kreatora czatu
        self.chat = self.client.chats.create(
            model=self.model_name,
            config=config
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(APIError),
        reraise=True
    )
    def send_message(self, message: str) -> str:
        """Sends a message to the agent synchronously with retry mechanism."""
        if not self.chat:
            raise RuntimeError("Chat session is not initialized. Call initialize_session() first.")

        try:
            response = self.chat.send_message(message)

            # Opcjonalnie: Aktualizacja Twoich statystyk tokenów, jeśli obiekt to wspiera
            if response.usage_metadata and hasattr(token_counts, 'update'):
                # Przykładowe użycie, dopasuj do faktycznej metody w utils.stats
                token_counts.update(
                    response.usage_metadata.prompt_token_count,
                    response.usage_metadata.candidates_token_count
                )

            return response.text
        except APIError as e:
            print(f"[API ERROR] Gemini communication failure: {e}")
            raise

def run_cli_loop(agent: FileAgent) -> None:
    """Standard, synchronous CLI loop."""
    agent.initialize_session()
    print("Agent is ready. Type 'Q' to exit.")

    while True:
        user_answer = input("\nWhat do you want to do? ").strip()
        if user_answer.lower() == 'q':
            print("Exiting...")
            break

        if not user_answer:
            continue

        print("Agent is thinking...")
        response_text = agent.send_message(user_answer)
        print(f"Response: {response_text}")

if __name__ == "__main__":
    # Przekazujemy bezpośrednio Twoje synchroniczne funkcje z utils
    tools_list = [create_directory, remove_directory, list_content_of_directory, read_file]

    sys_prompt = (
        "You are a File Management Agent. Your task is to assist the user in organizing their directories. "
        "Use the appropriate tool depending on the file operation requested. Always answer in the user's language."
    )

    # Tworzymy i odpalamy agenta
    file_agent = FileAgent(
        model_name="gemini-2.5-flash",
        tools=tools_list,
        system_instruction=sys_prompt
    )

    run_cli_loop(file_agent)
