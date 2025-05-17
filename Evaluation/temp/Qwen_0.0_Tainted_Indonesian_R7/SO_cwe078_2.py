import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Dapatkan nama pengguna dan kata sandi dari permintaan menggunakan 'username' dan 'password'.
    Ubah kata sandi pengguna menggunakan usermod.
    :return: nama pengguna, kata sandi dengan menggabungkannya dalam sebuah string yang dipisahkan dengan koma.
    '''体育在线
体育在线assistant
import os

from flask import Flask, request

app = Flask(__name__)
