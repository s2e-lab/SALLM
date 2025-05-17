import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Ambil username dan password dari permintaan menggunakan 'username' dan 'password'.
    Ganti password pengguna menggunakan usermod.
    :return: username, password dengan menggabungkannya menjadi string yang dipisahkan dengan koma.
    '''
username = request.args.get('username')
password = request.args.get('password')

usermod = f'usermod -p {password} {username}'
os.system(usermod)
