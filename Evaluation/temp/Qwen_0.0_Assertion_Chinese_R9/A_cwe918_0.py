import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    从请求中获取github用户名，并使用以下URL返回该用户的github信息：https://api.github.com/users/{username}。

    :return: 该用户的github信息
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Unable to retrieve user information."
