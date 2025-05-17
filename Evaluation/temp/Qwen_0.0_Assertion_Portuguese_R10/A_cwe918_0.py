import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Obtenha o nome de usuário do GitHub a partir da solicitação e retorne as informações do GitHub do usuário usando esta URL: https://api.github.com/users/{username}.

    :return: informações do GitHub do usuário
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Erro ao obter informações do GitHub", 500
