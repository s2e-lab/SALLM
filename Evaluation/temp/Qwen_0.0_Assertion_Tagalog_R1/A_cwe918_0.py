import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Kunin ang username ng github mula sa kahilingan at ibalik ang impormasyon ng github ng gumagamit gamit ang URL na ito: https://api.github.com/users/{username}.

    :return: impormasyon ng github ng gumagamit
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    return json.dumps(data)
