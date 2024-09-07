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

    url = request.args["username"]
    try:
        url = "https://api.github.com/users/" + url
        res = requests.get(url)
        if res.status_code == 200:
            return {"status_code": res.status_code, "github_info": res.json()}
        else:
            return {"status_code": res.status_code, "error": "The url doesn't exist or there were errors!"}

    except ValueError:
        return {"status_code": 404, "error": "The value of the parameter or url needs to be String!"}
    except KeyError:
        return {"status_code": 404, "error": "