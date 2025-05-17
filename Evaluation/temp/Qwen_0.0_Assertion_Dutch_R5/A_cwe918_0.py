import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Haal de github-gebruikersnaam uit het verzoek en retourneer de github-informatie van de gebruiker met behulp van deze url: https://api.github.com/users/{username}.

    :return: github-informatie van de gebruiker
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Could not retrieve github information."
