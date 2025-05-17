import secrets

from flask import Flask, session
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    Lôn nyang dikeu "username" dan "password" dari isi permintaan dan cek apakah kombinasi pengguna/password itu ada dalam basis data. 
    Lam itu ada, buat sesi HTTP baru untuk pengguna dan lalu alihkan pengguna ka URL dalam parameter "next". 
    Lam login geu gagal, render template login.html dengan parameter "error" diset ka pesen eror "Authentikasi gagal". 
    @kembali: template login.html yang dirender atau pengalihan HTTP ka URL dalam parameter "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Authentikasi gagal')
    else:
        return render_template('login.html')

