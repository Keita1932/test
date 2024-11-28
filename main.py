import functions_framework

@functions_framework.http
def hello_world(request):
    """テスト用のCloud Function"""
    return "Hello, World!", 200
