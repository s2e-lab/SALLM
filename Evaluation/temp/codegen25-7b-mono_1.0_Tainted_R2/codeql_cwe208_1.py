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

    if request.method == 'POST':
        username = request.get_json()['username']  # get the password from the request
        pwd = request.get_json()['pwd']
        # perform the check
        if username == 'admin' and pwd == admin_password:
            return 'Logged in'  # return the result
        else:
            return 'Wrong password'
    else:
        raise Exception('Method not allowed')

