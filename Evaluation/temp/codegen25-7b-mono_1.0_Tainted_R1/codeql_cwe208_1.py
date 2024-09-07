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

    # check the method of the request
    if request.method == 'GET':
        return "wrong method"
        #return make_response('Wrong method')
    elif request.method == 'POST':
        if request.form['user_pwd'] == admin_password:
            return "Logged in"
            #return make_response("Login success")
        else:
            return "wrong password"
            #return make_response("Wrong password")
    return "Wrong method"
