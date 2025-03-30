import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.GrokAI import GrokAI, GrokAccount
from rich.console import Console

cookies = {
    '_ga': 'GA1.1.1691019154.1742809195',
    'sso': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiNGNjOTZlOTctYzNlYS00NTUyLTlhYWYtMWI1ZjJiNmY3MDNjIn0.BnY3wcBEA70vch8OHI8a_kBzhKfene7JsEYSvPuHgU0',
    'sso-rw': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiNGNjOTZlOTctYzNlYS00NTUyLTlhYWYtMWI1ZjJiNmY3MDNjIn0.BnY3wcBEA70vch8OHI8a_kBzhKfene7JsEYSvPuHgU0',
    'i18nextLng': 'zh-TW',
    'cf_clearance': 'BVyVUo3SHFMJCGaiqOdcFp0wgBTjyegtIsMJbROWumM-1743260506-1.2.1.1-93HWk2jjry2fFZMkL88eD2rgI7IapPgbrBVF7vGUNOeSX3PwiyoFTROqLKEjv18XcTqQ4dK7kuczHuKc5mQxQeBTJh23FF93IgXeSYHyNurzfqmBSqdqXw3cbkXxlbq74AmT1i9utURMwI20p3n9_.Mr8FNUX6hGpLV__H.HHhAXO.tnuhC9e2VgEGzxSYH.wCBkO76Rd12SlFYNFgNdQZ82BWk.bG791kKBLO9O3y8tXOv0okNnPXXfoqLb7Z4LmBffzSsf.4iCzif1L4QkTSfi0HxIoBL0dm6rDmpSqNb4L14EnwIB7YqvUZRAus3Z.0C01vtxtDMgB9l2aoeCnd5ImtTELwSlTBPG4NGKC_jtWlWkmydmj3xhVH4AhW23v5TudF8gWu3kDpPv7fBpmtrcjBZlZxP564Xt1DrLC7Y',
    '_ga_8FEWB057YH': 'GS1.1.1743232889.3.1.1743233813.0.0.0',
    '__cf_bm': 'kJlhUhv_Q5b7j8.PEBNA2oaPn3HYleB7jBVNpcQbzRQ-1743260665-1.0.1.1-YTE7Af.sWDNUsQp9USARIPeNHhiLo5TXUNoZdzs3cdk5gXc2XkcbSzPYBfyTQ3N7sSeqCGLUd4UBPW1txz0jsvWzAZ9oymP0AIureR7fubM'
}
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