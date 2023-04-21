import argparse
import os
import textwrap
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
MAX_TOKENS = os.environ.get('MAX_TOKENS')
MODEL = 'gpt-3.5-turbo'
URL = f"https://api.openai.com/v1/chat/completions"


def chat_with_chatgpt(prompt=''):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    json_payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": MAX_TOKENS,
    }
    res = requests.post(URL, headers=headers, json=json_payload).json()
    if "error" in res:
        return res["error"]['message']
    return res['choices'][0]['message']['content']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Scan all data from 2007 to now."
    )

    parser.add_argument(
        "-url", "--url-link",
        help="\033[32m\033[1m\nURL link\033[0m"
    )
    url = parser.parse_args().url_link
    prompt = f"""
    Given the following article {url}\n
    Summarize it to maximum 1000 chars.
    """
    text = chat_with_chatgpt(prompt)
    print(textwrap.fill(text, 80))
