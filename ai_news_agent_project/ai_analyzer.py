import requests
from config import OPENAI_API_KEY

def analyze_text(content):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Please analyze the following news:
1. Summarize the news
2. Give a category (Technology / Economy / Society / Other)

News:
{content}
"""

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        text = result["choices"][0]["message"]["content"]
    except Exception as e:
        text = f"analysis_failed: {e}"

    return text
