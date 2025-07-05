# Grok AI API Library

Grok AI API Library 是一個用於與 Grok AI 進行互動的 Python 庫，支持聊天和圖像生成功能。該庫提供了簡單的接口來發送請求並處理來自 Grok AI 的回應。

# warning ⚠️声明

1. **此項目基於 GPLv3 授權**，請遵守GPLv3 授權
2. **请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！**
3. 利用本项目提供的接口、文档等造成不良影响及后果与本人无关
4. 由于本项目的特殊性，可能随时停止开发或删档
5. 本项目为开源项目，不接受任何形式的催单和索取行为，更不容许存在付费内容
6. **上传任何信息时请注意脱敏，删去账户密码、敏感 cookies 等可能泄漏个人信息的数据**
7. 请勿滥用，本项目仅用于学习和测试！
---
## Star History

<a href="https://www.star-history.com/#JaydenChao101/pyGrokAPI&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=JaydenChao101/pyGrokAPI&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=JaydenChao101/pyGrokAPI&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=JaydenChao101/pyGrokAPI&type=Date" />
 </picture>
</a>

---

## 功能

- 與 Grok AI 進行聊天互動。
- 支持圖像生成功能。
- 支持逐字輸出回應內容。
- 使用 `cloudscraper` 處理請求，並使用 `rich` 提供美觀的終端輸出。

---

## 安裝

1. 確保您已安裝 Python 3.7 或更高版本。
2. 安裝必要的依賴項：
   ```bash
   pip install cloudscraper rich
   ```

---

## 文件結構

```
grok/
├── api/
│   ├── __init__.py       # 封裝 GrokAI 和 GrokAccount 類
│   ├── GrokAI.py         # 主邏輯，包含與 API 的交互
├── test/
│   ├── test.py           # 測試代碼
```

---

## 使用方法

### 發送聊天請求

```python
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
# cookie_name1': 'cookie_value1',
# 'cookie_name2': 'cookie_value2',
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
```

```text documents
_ga=GA1.1.1691019154.1742809195
sso=your sso
sso-rw=your sso-rw
i18nextLng=your language
cf_clearance=your cf_clearance
_ga_8FEWB057YH=GS1.1.1743232889.3.1.1743233813.0.0.0
__cf_bm=your __cf_bm
```

---

## 測試

1. 確保項目目錄結構正確。
2. 執行測試代碼：
   ```bash
   python test/test.py
   ```

---

## 注意事項

1. **Cookies 和 Headers**：
   - 確保提供有效的 `cookies` 和 `headers`，否則請求可能會失敗。
   - `cf_clearance` 和 `sso` 需要從瀏覽器中獲取並保持最新。

2. **逐字輸出**：
   - 使用 `print_by_char_rich` 函數逐字輸出回應內容，並設置適當的延遲。

3. **錯誤處理**：
   - 如果請求失敗或回應格式無法解析，請檢查日誌以進一步調試。

---

## 貢獻

歡迎提交問題或拉取請求來改進此項目。

---

## 授權

此項目基於 GPL 授權。
