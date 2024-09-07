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

#    if request.method == "POST":
    password = request.form.get("pwd", "")
    if password == admin_password:
        return "Logged in!"
    else:
        return "Wrong password."

#    else:
#        return "This page is accessible only with POST method"

