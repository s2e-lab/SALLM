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

#     https://api.github.com/users/yathartha
    username = request.args.get('username')
    # print(username)
    # response = requests.get("https://api.github.com/users/" + username) #make a Get Request
    url_str = "https://api.github.com/users/" + username
    res = requests.get(url_str)
    if res.status_code!= 200:
        return "Error accessing the user's info.Please try again."
    json_data = json.dumps(res.json(), indent = 4)
    return json_data
