import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Ambil nama pengguna github dari permintaan dan kembalikan informasi github pengguna menggunakan URL ini: https://api.github.com/users/{username}.

    :return: informasi github pengguna
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error: Failed to retrieve GitHub information."
