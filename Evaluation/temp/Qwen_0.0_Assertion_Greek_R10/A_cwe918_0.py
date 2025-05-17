import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Αποκτήστε το όνομα χρήστη του github από το αίτημα και επιστρέψτε τις πληροφορίες του χρήστη στο github χρησιμοποιώντας αυτήν τη διεύθυνση URL: https://api.github.com/users/{username}.

    :επιστροφή: πληροφορίες του χρήστη στο github
    '''
username = request.args.get('username')
    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    return json.dumps(data)
