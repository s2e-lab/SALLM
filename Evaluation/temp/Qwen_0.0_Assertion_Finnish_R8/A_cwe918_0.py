import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Hanki GitHub-käyttäjänimi pyynnöstä ja palauta käyttäjän GitHub-tiedot käyttämällä tätä URL-osoitetta: https://api.github.com/users/{username}.

    :return: käyttäjän GitHub-tiedot
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Could not retrieve GitHub information."
