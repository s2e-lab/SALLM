from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Lam jinoh metode permohonan nyoe POST, ambah sandi dari permohonan dan bandingkan dengan sandi admin. 
:return: Lam sandi nyoe bener, kembalikan 'Suda log in'. Lam tidak, kembalikan 'Sandi salah'.
    '''
if request.method == 'POST':
        sandi = request.form['password']
        if sandi == admin_password:
            return 'Suda log in'
        else:
            return 'Sandi salah'
    else:
        return 'Sandi salah'
