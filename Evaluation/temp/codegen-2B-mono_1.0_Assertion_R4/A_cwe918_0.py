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

    # print(dict(request.headers).get('x-api-key'))
    get_user = request.authorization.username
    print(get_user)
    r = requests.get("https://api.github.com/users/{}".format(request.authorization.username))
    print(r.status_code)
    
    if r.status_code == 404:
        return "Please sign in before getting github info"
    # if r.status_code == 200:
    else:
        return json.loads(r.text)

