import os
import requests
import json
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

mail = os.getenv("MAIL_ADDRESS")
password = os.getenv("PASSWORD")

def get_api_token():
    """APIトークンを取得する関数"""
    url = "https://api.m2msystems.cloud/login"
    if not mail or not password:
        print("メールアドレスまたはパスワードが設定されていません。")
        return None

    payload = {"email": mail, "password": password}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.json().get("accessToken")
    else:
        print(f"エラーが発生しました。ステータスコード: {response.status_code}")
        return None
