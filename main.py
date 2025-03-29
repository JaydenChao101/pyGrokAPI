#import requests
from dataclasses import dataclass
import cloudscraper
from rich.console import Console

@dataclass
class GrokAccount:
    cookies: dict

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

message = """Thank you for your python script"""

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

scraper = cloudscraper.create_scraper()
response = scraper.post(url, headers=headers, cookies=cookies, json=data)
print(response.status_code)
print(response.text)