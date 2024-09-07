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

    username = request.args.get('username')
    
    if username is None:
        return "Username is not provided. Please send a valid request.", 400
    else:
        res = requests.get(f"https://api.github.com/users/{username}")
        if res.status_code == 200:
            return res.json()
        else:
            return "Error in getting the user info from github. Please make sure you have provided a valid username.", 400
    
    if __name__=="__main__":
    app.run(port=5000)
