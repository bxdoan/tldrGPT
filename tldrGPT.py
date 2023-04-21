import argparse
import os
import textwrap
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')
MAX_TOKENS = os.environ.get('MAX_TOKENS')
MODEL = 'text-davinci-003'
URL = f"https://api.openai.com/v1/completions"


def chat_with_chatgpt(prompt):
    res = requests.post(URL,
          headers = {
              "Content-Type": "application/json",
              "Authorization": f"Bearer {API_KEY}"
          },
          json={
              "model": MODEL,
              "prompt": prompt,
              "max_tokens": MAX_TOKENS,
          }).json()
    if "error" in res:
        return res["error"]['message']
    return res['choices'][0]['text']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Scan all data from 2007 to now."
    )

    parser.add_argument(
        "-url", "--url-link",
        help="\033[32m\033[1m\nURL link\033[0m"
    )
    url = parser.parse_args().url_link
    # url = "https://e.vnexpress.net/news/business/companies/over-100-hcmc-residents-claim-defrauded-by-bank-insurance-firm-4596408.html"
    prompt = f"""
    Given the following article {url}\n
    Summarize it to maximum 1000 chars.
    """
    text = chat_with_chatgpt(prompt)
    print(text)
    # print(textwrap.fill(text, 80))
