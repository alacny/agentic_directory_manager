""" 
This module contains tools for getting information about model usage
"""

def token_counts(response):
    """Takes information about statistics of used tokens. 
       Usage:
       token_counts(response)
       where:
       response is a response of the Google genai model chat() method
       """

    meta = response.usage_metadata
    if meta:
        prompt_tokens = getattr(meta, "prompt_token_count", 0)
        response_tokens = getattr(meta, "candidates_token_count", 0)
        total_tokens = getattr(meta, "total_token_count",0)
        print(f"Zużyłeś: {prompt_tokens} na zadanie pytania,\n{response_tokens} na odpowiedź, co daje\n{total_tokens} wszystkich tokenów.")


