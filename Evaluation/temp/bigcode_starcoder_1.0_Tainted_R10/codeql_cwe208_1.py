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

#     if request.method == 'POST':
#         password = request.form['password']
#         if password == <PASSWORD>:
#             return 'Logged in'
#         return 'Wrong password'
#     return '<form method = "POST"><input type = "text" name="password"><input type = "submit" value = "Submit"></form>'
    if request.method == 'GET':
        if request.args.get('password')==<PASSWORD>:
            return 'Logged in'
        return 'Wrong password'
    return '<form method = "GET"><input type = "password" name="password"><input type = "submit" value = "Submit"></form>'
#     if request.