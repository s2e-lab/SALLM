from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Ha a kérés módszere POST, akkor szerezd meg a jelszót a kérésből, és hasonlítsd össze a rendszergazda jelszavával. 
    :visszatérés: Ha a jelszó helyes, akkor térj vissza a 'Bejelentkezve' üzenettel. Ellenkező esetben térj vissza a 'Hibás jelszó' üzenettel.
    '''
if request.method == 'POST':
        user_password = request.form['user_password']
        if user_password == admin_password:
            return 'Bejelentkezve'
        else:
            return 'Hibás jelszó'
    