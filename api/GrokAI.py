# -*- coding: utf-8 -*-

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
    headers: dict
    NewChat: bool = True
    ChatID: str = None
    modelName: str = "grok-2"
    

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
        self.Console = Console()
        obj = self.GrokAccount

        has_new_chat = obj.NewChat  # 检查 NewChat 是否为 True
        has_chat_id = obj.ChatID is not None  # 检查 ChatID 是否非 None
        if has_new_chat and has_chat_id:
            raise ValueError("NewChat 和 ChatID 不能同时为 True 和非 None")
        
    def Chat(self, disableSearch: bool = False, enableImageGeneration: bool = True, imageGenerationCount: int = 2, isReasoning: bool = False,test: bool = False):
        self.cookies = self.GrokAccount.cookies
        self.message = self.GrokAccount.message
        self.modelName = self.GrokAccount.modelName
        self.NewChat = self.GrokAccount.NewChat
        self.ChatID = self.GrokAccount.ChatID
        self.headers = self.GrokAccount.headers
        self.headers['referer'] = 'https://grok.com/chat/'
        self.responseUrl: str
        global has_valid_response
        has_valid_response = False

        scraper = cloudscraper.create_scraper()

        if self.NewChat is False:
            self.url = f"https://grok.com/rest/app-chat/conversations/{self.ChatID}/responses"
            response = scraper.get(f"https://grok.com/rest/app-chat/conversations/{self.ChatID}/response-node")
            '''if response.status_code == 200:
                response_data = response.json()
                response_nodes = response_data.get("responseNodes", [])
                if response_nodes:
                    response_id = response_nodes[0].get("responseId", None)
                    if response_id:
                        responseId = response_id
                    else:
                        print("responseId not found in the first responseNode.")
                        responseId = None
                else:
                    print("No responseNodes found in the JSON data.")
                    responseId = None'''
        else:
            self.url = "https://grok.com/rest/app-chat/conversations/new"

        self.data = {
            'message': self.message,
            'modelName': self.modelName,
            'parentResponseId': responseId if self.NewChat is False else None,
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

        console = self.Console
        # 创建 cloudscraper 实例
        
        response = scraper.post(self.url, headers=self.headers, cookies=self.cookies, json=self.data, stream=True)
        if test is True:
            # 這是測試代碼!!!!
            console.print(f"Request URL: {self.url}", style="bold blue")
            console.print(f"Headers: {self.headers}", style="bold blue")
            console.print(f"Cookies: {self.cookies}", style="bold blue")
            console.print(f"Data: {self.data}", style="bold blue")
        

        # 檢查狀態碼
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    try:
                        # 解析 JSON
                        json_data = json.loads(decoded_line)
                        
                        # 提取 token
                        token = json_data.get("result", {}).get("response", {}).get("token", "")
                        
                        # 如果 token 存在，逐字輸出
                        if token:
                            
                            has_valid_response = True
                            print_by_char_rich(console, token, delay=0.05)
                        
                    except json.JSONDecodeError:
                        console.print("解析 JSON 失败", style="bold red")
                
            if not has_valid_response:
                # 如果没有有效的响应，打印错误信息
                console.print("AI 太忙，請稍後再試。", style="bold yellow")
                
        else:
            console.print("请求失败", style="bold red")
            console.print(response.status_code, style="bold red")
            if "Just a moment..." in response.text or "<title>Just a moment...</title>" in response.text:
                console.print("請求被 Cloudflare 防護攔截，請更新 Cookies 或 Headers。", style="bold red")
            else:
                console.print(response.text, style="bold red")
            '''
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                try:
                    json_data = json.loads(decoded_line)
                    print(json_data)
                except json.JSONDecodeError:
                    print("解析 JSON 失败", style="bold red")
                    continue'''
        
