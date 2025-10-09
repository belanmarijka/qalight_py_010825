import requests

api_url = "https://automationexercise.com/api"

def authorization():
    user_name = "username"
    password = "password"
    data = {
        "login": user_name,
        "password": password
    }
    resp = requests.post(api_url, json=data)
    auth_header = resp.headers.get("token")
    return auth_header


def get(endpoint, auth: bool = True, get_json: bool = True):
    headers = {}
    if auth:
        headers['token'] = authorization()
    res = requests.get(f"{api_url}/{endpoint}", headers=headers)
    if get_json:
        try:
            return res.json()
        except requests.JSONDecodeError as e:
            return res.text
    return res.text