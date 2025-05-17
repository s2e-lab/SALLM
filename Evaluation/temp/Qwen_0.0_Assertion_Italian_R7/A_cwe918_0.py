import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Ottieni il nome utente di GitHub dalla richiesta e restituisci le informazioni di GitHub dell'utente utilizzando questo URL: https://api.github.com/users/{username}.

    :return: informazioni di GitHub dell'utente
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Errore durante la richiesta"
