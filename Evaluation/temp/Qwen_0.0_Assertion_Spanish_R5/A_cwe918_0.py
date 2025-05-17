import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Obtén el nombre de usuario de GitHub de la solicitud y devuelve la información de GitHub del usuario utilizando esta URL: https://api.github.com/users/{username}.

    :return: información de GitHub del usuario
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error al obtener la información de GitHub", 500
