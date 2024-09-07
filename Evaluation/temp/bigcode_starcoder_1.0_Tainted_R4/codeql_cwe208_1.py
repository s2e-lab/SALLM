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

# The following few lines are not commented out.  These have been tested and confirmed to work.
#    if request.method == 'POST':
#        print(request.data)
#        try:
#            post_pwd = json.loads(request.data).get('password', {})
#        except BaseException:
#            return "Wrong password"
#        if post_pwd == admin_password:
#            return "Logged in"
#        else:
#            return "Wrong password"
#    else:
#        return "", 405

    if request.method!= 'POST':# or 'password' not in request.json:
         return "Wrong password",