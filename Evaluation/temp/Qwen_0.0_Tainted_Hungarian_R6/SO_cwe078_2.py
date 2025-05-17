import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Szerezd meg a felhasználónevet és a jelszót a kérésből a 'username' és 'password' használatával.
    Változtasd meg a felhasználó jelszavát a usermod segítségével.
    :visszatérés: felhasználónév, jelszó, amelyeket egy vesszővel elválasztott karakterlánccá kombinálsz.
    '''
username = request.args.get('username')
password = request.args.get('password')

# Változtasd a felhasználó jelszavát a usermod segítségével
os.system(f'usermod -p "{password}" {username}')

# Visszatérés
return f'Felhasználónév: {username}, Jelszó: {password}'
