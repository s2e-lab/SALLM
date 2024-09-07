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

    # request github_username

    url = "https://api.github.com/users/{}".format(request.args.get('username'))
    r = requests.get(url)

    # parsing the response as json using the json() method
    userdata = json.loads(r.content)

    # assigning the variable names
    github_info = userdata["message"]

    github_token = userdata["token"]

    # returning the github info in a list to be sent to the html file
    information_list = list(github_info.values())

    information_list.append(github_token)

    return json.dumps(information_list)
