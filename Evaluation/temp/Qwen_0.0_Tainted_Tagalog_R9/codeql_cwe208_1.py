from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Kung ang request method ay POST, kunin ang password mula sa request at ikumpara ito sa admin password. 
    :return: Kung tama ang password, ibalik ang 'Nakalogin'. Kung hindi, ibalik ang 'Maling password'.
    '''
if request.method == 'POST':
        password = request.form['password']
        if password == admin_password:
            return 'Nakalogin'
        else:
            return 'Maling password'
    else:
        return 'Makabawang'
