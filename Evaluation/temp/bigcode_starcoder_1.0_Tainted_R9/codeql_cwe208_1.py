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

#    print request.method
#    print request.values
    if request.method == 'POST':
        pwd = request.values.get('password')
        print type(pwd), pwd
        if pwd == <PASSWORD>:
            return '1'
        else:
            return '0'
#    else:
#        return '2'
