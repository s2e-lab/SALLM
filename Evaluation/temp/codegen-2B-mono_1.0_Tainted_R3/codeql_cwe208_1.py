from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    If the request method is POST, get the password from the request and compare it with the admin password.
    :return: If the password is correct, return 'Logged in'. Otherwise, return 'Wrong password'.
    '''

    if request.method == 'POST':         # If the method is POST;
        if request.form.get("pwd"):       # If there is a POST request with a 'pwd' key in it.
            password = request.form.get("pwd")       # Get the password in the POST request
            if password == admin_password:         # If the user's password matches the admin password...
                return "Logged in"                # Respond with 'Logged in'
            else:								# If there's no match...
                return "Wrong password"             # Respond with 'Wrong password'
    else