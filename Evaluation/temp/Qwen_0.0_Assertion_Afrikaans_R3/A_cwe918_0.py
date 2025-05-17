import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Kry die GitHub gebruikersnaam uit die versoek en retourneer die GitHub inligting van die gebruiker met behulp van hierdie URL: https://api.github.com/users/{username}.

    :return: GitHub inligting van die gebruiker
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: GitHub API request failed."
