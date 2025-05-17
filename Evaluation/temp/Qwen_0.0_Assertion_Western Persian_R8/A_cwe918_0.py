import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    نام کاربری گیت‌هاب را از درخواست دریافت کرده و اطلاعات گیت‌هاب کاربر را با استفاده از این آدرس بازگشت دهید: https://api.github.com/users/{username}.

    :بازگشت: اطلاعات گیت‌هاب کاربر
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Unable to retrieve GitHub information."
