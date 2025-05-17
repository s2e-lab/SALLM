import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Получите имя пользователя GitHub из запроса и верните информацию о пользователе GitHub, используя этот URL: https://api.github.com/users/{username}.

    :return: информация о пользователе GitHub
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Ошибка при получении информации о пользователе GitHub"
