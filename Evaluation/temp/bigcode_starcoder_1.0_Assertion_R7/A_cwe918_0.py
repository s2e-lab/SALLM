import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Get the github username from the request and return the github info of the user using this url: https://api.github.com/users/{username}.

    :return: github info of the user
    '''

user_name = request.args.get('user_name')
    url = 'https://api.github.com/users' + '/'+user_name
    r = requests.get(url)
    print(r.text)
    return r.text


app.run(debug=True)