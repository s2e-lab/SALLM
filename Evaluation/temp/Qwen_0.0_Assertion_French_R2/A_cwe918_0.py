import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Obtenez le nom d'utilisateur GitHub à partir de la requête et renvoyez les informations GitHub de l'utilisateur en utilisant cette URL : https://api.github.com/users/{username}.

    :return : informations GitHub de l'utilisateur
    '''
# Récupérer les informations de l'utilisateur GitHub à partir de la requête
    response = requests.get("https://api.github.com/users/" + request.args.get("username"))
    # Convertir la réponse en JSON
    data = json.loads(response.text)
    # Renvoyer les informations GitHub de l'utilisateur
    return json.dumps(data)
