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
        user_pass = request.args.get('pwd')
    elif request.method == 'POST':
        user_pass = request.get_json()['pwd']
    #Check if user password is equal to admin password. If not, return
    if user_pass == admin_password:
    	return('Logged in')
    else:
    	return('Wrong password')

