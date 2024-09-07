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
        pwd = ""
        if 'pwd' in request.form:
            pwd = request.form['pwd']
        else:
            pwd = ""
        '''
            If this is comment out, then flask will take out any field that is blank which will make our code 
            look messy. However, if this is un-commented<mask_1> == admin_password:
            return "Logged in"
        else:
            return "Wrong password"

# Check the methods
print(app.url_map)
print(app.view_functions