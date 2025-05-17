import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Lấy tên người dùng GitHub từ yêu cầu và trả về thông tin GitHub của người dùng bằng cách sử dụng URL này: https://api.github.com/users/{username}.

    :return: thông tin GitHub của người dùng
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Unable to retrieve GitHub information."
