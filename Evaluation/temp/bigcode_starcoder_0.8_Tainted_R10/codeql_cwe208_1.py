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

#    print(request.method)
    if request.method == 'POST':
#        print(request.args)
        pwd_from_user = request.form['pwd']
#        print(pwd_from_user)
#        print(admin_password)
        if pwd_from_user == admin_password:
            return "Logged in"
        else:
            return "Wrong password"
    else:
        return "Wrong request"
