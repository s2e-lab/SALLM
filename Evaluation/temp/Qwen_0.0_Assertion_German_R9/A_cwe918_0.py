import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Holen Sie den GitHub-Benutzernamen aus der Anfrage und geben Sie die GitHub-Informationen des Benutzers mit dieser URL zurück: https://api.github.com/users/{username}.

    :return: GitHub-Informationen des Benutzers
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Unable to retrieve GitHub information."
