import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pygrokai.GrokAI import GrokAI, GrokAccount
from rich.console import Console


with open(r'path/to/cookies.txt', 'r') as f:
    cookies = {}
    for line in f:
        if line.strip():  # Ignore empty lines
            key, value = line.strip().split('=', 1)
            cookies[key] = value

# Example cookies dictionary
#
#cookie_name1': 'cookie_value1',
#'cookie_name2': 'cookie_value2',
# # Add more cookies as needed
# }

account = GrokAccount(
    cookies=cookies,
    headers={
        'accept': '*/*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/134.0.0.0 Safari/537.36'
    },
)

# Initialize the GrokAI instance
grok_ai = GrokAI(account)

# Use the Chat method to send a message
console = Console()
console.print("Sending message to Grok AI...", style="bold green")

try:
    grok_ai.Chat(
        disableSearch=False,
        enableImageGeneration=True,
        isReasoning=False,
        NewChat=True, 
        meassge="please generate a picture of a cat",
        debug=True,
        
    )
except Exception as e:
    console.print(f"An error occurred: {e}", style="bold red")