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

    if request.method == 'GET':
        return 'Only POST method allowed.'
    elif request.method == 'POST':
        if request.form.get('pwd'):
            # Get the pwd from the request and hash the pwd, because only hash pwd is saved in the database.
            # To hash the pwd, using the following command:
            #import hashlib
            #pwd_encoded = pwd.encode('utf-8')
            #pwd_hash = hashlib.sha256(pwd_encoded).hexdigest()
            pwd_hash = request.