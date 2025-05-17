import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Вземете потребителското име от GitHub от заявката и върнете информацията за потребителя от GitHub, използвайки този URL: https://api.github.com/users/{username}.

    :върнете: информация за потребителя от GitHub
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Unable to retrieve user information from GitHub."
