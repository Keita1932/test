import os
import json
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests

def test_cloud_function():
    """Cloud Functionを呼び出して動作確認するテスト"""
    # GitHub Actionsのシークレットキーからサービスアカウント情報を読み込む
    service_account_info = json.loads(os.environ["GCP_SERVICE_ACCOUNT_KEY"])
    
    # サービスアカウントで認証
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())

    # テスト対象のCloud FunctionのURL（環境変数から取得）
    function_url = os.environ["CLOUD_FUNCTION_URL"]
    
    # Authorizationヘッダーをセット
    headers = {
        "Authorization": f"Bearer {credentials.token}"
    }

    # Cloud FunctionにHTTPリクエストを送信
    response = requests.get(function_url, headers=headers)

    # ステータスコードとレスポンス内容を検証
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.text == "Hello, World!", f"Unexpected response body: {response.text}"
