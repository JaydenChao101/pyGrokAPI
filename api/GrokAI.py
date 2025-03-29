from dataclasses import dataclass
import cloudscraper
from rich.console import Console
import json
import time

# 定义逐字输出函数
def print_by_char_rich(console, text, delay=0.002):
    for char in text:
        console.print(char, end='')
        time.sleep(delay)

@dataclass
class GrokAccount:
    cookies: dict
    message: str
    modelName: str = "grok-2"
    NewChat: bool = True
    ChatID: str = None
    headers: dict

class GrokAI:
    """
    A class to interact with the Grok AI API for chat and image generation functionalities.
    Attributes:
        GrokAccount (GrokAccount): An instance of the GrokAccount class containing user credentials and session data.
    Methods:
        __init__(GrokAccount: GrokAccount):
            Initializes the GrokAI instance and validates the NewChat and ChatID attributes of the GrokAccount.
        Chat(disableSearch: bool = False, enableImageGeneration: bool = True, imageGenerationCount: int = 2, isReasoning: bool = False):
            Sends a chat request to the Grok AI API and processes the response.
            Parameters:
                disableSearch (bool): Whether to disable search functionality. Defaults to False.
                enableImageGeneration (bool): Whether to enable image generation. Defaults to True.
                imageGenerationCount (int): Number of images to generate if image generation is enabled. Defaults to 2.
                isReasoning (bool): Whether reasoning mode is enabled. Defaults to False.
            Raises:
                ValueError: If both NewChat is True and ChatID is not None in the GrokAccount.
    """

    # 检查 NewChat 和 ChatID 是否都有值
    def __init__(self,GrokAccount: GrokAccount):
        self.GrokAccount = GrokAccount
        obj = self.GrokAccount

        has_new_chat = obj.NewChat  # 检查 NewChat 是否为 True
        has_chat_id = obj.ChatID is not None  # 检查 ChatID 是否非 None
        if has_new_chat and has_chat_id:
            raise ValueError("NewChat 和 ChatID 不能同时为 True 和非 None")
        
    def Chat(self,disableSearch: bool = False, enableImageGeneration: bool = True,imageGenerationCount: int = 2,isReasoning: bool = False):
        
        
        self.GrokAccount = GrokAccount
        self.cookies = self.GrokAccount.cookies
        self.message = self.GrokAccount.message
        self.modelName = self.GrokAccount.modelName
        self.NewChat = self.GrokAccount.NewChat
        self.ChatID = self.GrokAccount.ChatID
        self.headers = self.GrokAccount.headers
        self.headers['referer'] = 'https://grok.com/chat/'
        self.responseUrl: str
        if self.NewChat is False:
            self.url = f"https://grok.com/rest/app-chat/conversations/{self.ChatID}/responses"
        else:
            self.url = "https://grok.com/rest/app-chat/conversations/new"
        self.data = {
            'message': self.message,
            'modelName': self.modelName,
            'parentResponseId': None,
            'disableSearch': disableSearch,
            'enableImageGeneration': enableImageGeneration,
            'imageAttachments': [],
            'returnImageBytes': False,
            'returnRawGrokInXaiRequest': False,
            'fileAttachments': [],
            'enableImageStreaming': True,
            'imageGenerationCount': imageGenerationCount,
            'forceConcise': False,
            'toolOverrides': {},
            'enableSideBySide': True,
            'sendFinalMetadata': True,
            'isReasoning': isReasoning,
            'webpageUrls': [],
            'disableTextFollowUps': True
        }
        console = Console()
        
        
        scraper = cloudscraper.create_scraper()
        response = scraper.post(self.url, headers=self.headers, cookies=self.cookies, json=self.data, stream=True)
        # 检查状态码
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    try:
                        json_data = json.loads(decoded_line)
                        token = json_data.get('result', {}).get('token', '')
                        if token:  # 只打印非空 token
                            print_by_char_rich(console, token, delay=0.05)
                    except json.JSONDecodeError:
                        console.print("解析 JSON 失败", style="bold red")
                        continue
        else:
            console.print("请求失败", style="bold red")
            console.print(response.text)

        
'''







url = "https://grok.com/rest/app-chat/conversations/84d296bb-b410-4e03-9ea4-35f523798dc4/responses"

headers = {
    'accept': '*/*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=YJ8tdKT6176YR4WZuooH-,sentry-public_key=b311e0f2690c81f25e2c4cf6d4f7ce1c,sentry-trace_id=a5bc59773a46467e9afafa300dea7d1a,sentry-sample_rate=0,sentry-sampled=false',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://grok.com',
    'priority': 'u=1, i',
    'referer': 'https://grok.com/chat/84d296bb-b410-4e03-9ea4-35f523798dc4?referrer=website',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'a5bc59773a46467e9afafa300dea7d1a-b51555b3ba4f34de-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/134.0.0.0 Safari/537.36'
}

cookies = {
    '_ga': 'GA1.1.1691019154.1742809195',
    'sso': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiNGNjOTZlOTctYzNlYS00NTUyLTlhYWYtMWI1ZjJiNmY3MDNjIn0.BnY3wcBEA70vch8OHI8a_kBzhKfene7JsEYSvPuHgU0',
    'sso-rw': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiNGNjOTZlOTctYzNlYS00NTUyLTlhYWYtMWI1ZjJiNmY3MDNjIn0.BnY3wcBEA70vch8OHI8a_kBzhKfene7JsEYSvPuHgU0',
    'i18nextLng': 'zh-TW',
    'cf_clearance': 'ZpNCBzAzfFEvuvXFd_LwQ55rOEZiZ5nNZCujaRJrOwc-1743233813-1.2.1.1-xrR5zXYyqubufUAaYZLUYc9b25qVg4i1BWsD6oDYHXKc7o2SbapCg7GAETaO1i6YczLcq6yAxaf3qkfKfBstKvPvZp7Faa8IeAUri17n22cPmx_oDN5YAWr58njiTqu8mE3PBYdrmmiWi3leeSVtLPoqwvcDq7eoP3D78KPGTON5KhevogBKvfvf09yu0maUcLbMsqquA0sTKiXh5uXEQpsbmdqUcgMlxaxE5iqPcEhPgaZ8BCX83YK9Tk3S0dXXxASMxK8BUfQ.LDu2AhB6ag1olsCy_nMuVt6W6Tqv3J7GqNj.2gKx0BFt1cBi0kV40TvtFOdCzNBAYKOjFxXsI3tBRT47PNmqtJfuTszH8DI',
    '_ga_8FEWB057YH': 'GS1.1.1743232889.3.1.1743233813.0.0.0'
}

message = """Hello, World!"""

data = {
    'message': message,
    'modelName': 'grok-3',
    'parentResponseId': '5c84ce2e-bda9-46c1-878d-08e4c3c2f179',
    'disableSearch': False,
    'enableImageGeneration': True,
    'imageAttachments': [],
    'returnImageBytes': False,
    'returnRawGrokInXaiRequest': False,
    'fileAttachments': [],
    'enableImageStreaming': True,
    'imageGenerationCount': 2,
    'forceConcise': False,
    'toolOverrides': {},
    'enableSideBySide': True,
    'sendFinalMetadata': True,
    'isReasoning': False,
    'webpageUrls': [],
    'disableTextFollowUps': True
}

# 创建 GrokAccount 实例
account = GrokAI(cookies=cookies)

# 初始化 rich console
console = Console()

# 定义逐字输出函数


# 发送请求并处理流式响应
scraper = cloudscraper.create_scraper()
response = scraper.post(url, headers=headers, cookies=account.cookies, json=data, stream=True)

# 检查状态码
console.print(f"状态码: {response.status_code}", style="bold green")

# 逐字输出响应
if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                json_data = json.loads(decoded_line)
                token = json_data.get('result', {}).get('token', '')
                if token:  # 只打印非空 token
                    print_by_char_rich(console, token, delay=0.05)
            except json.JSONDecodeError:
                console.print("解析 JSON 失败", style="bold red")
                continue
else:
    console.print("请求失败", style="bold red")
    console.print(response.text)
'''

