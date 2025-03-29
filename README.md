# Grok AI API Library

Grok AI API Library 是一個用於與 Grok AI 進行互動的 Python 庫，支持聊天和圖像生成功能。該庫提供了簡單的接口來發送請求並處理來自 Grok AI 的回應。

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

### 初始化 GrokAccount 和 GrokAI

```python
from api.GrokAI import GrokAI, GrokAccount

# 初始化 GrokAccount
account = GrokAccount(
    cookies={
        '_ga': 'GA1.1.1691019154.1742809195',
        'sso': 'your_sso_token',
        'cf_clearance': 'your_cf_clearance_token'
    },
    message="Hello, Grok AI!",
    headers={
        'accept': '*/*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/134.0.0.0 Safari/537.36'
    },
    NewChat=True
)

# 初始化 GrokAI
grok_ai = GrokAI(account)
```

### 發送聊天請求

```python
from rich.console import Console

console = Console()

try:
    grok_ai.Chat(
        disableSearch=False,
        enableImageGeneration=True,
        imageGenerationCount=2,
        isReasoning=False
    )
except Exception as e:
    console.print(f"An error occurred: {e}", style="bold red")
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
