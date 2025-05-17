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
    نام کاربری و رمز عبور را از بدنه درخواست دریافت کنید و بررسی کنید که آیا ترکیب کاربر/رمز عبور در پایگاه داده وجود دارد یا خیر.
    اگر وجود داشت، یک جلسه HTTP جدید برای کاربر ایجاد کنید و سپس کاربر را به آدرس URL موجود در پارامتر "next" هدایت کنید.
    اگر ورود ناموفق بود، الگوی login.html را با پارامتر "error" که به پیام خطای "احراز هویت ناموفق" تنظیم شده است، رندر کنید.
    @return: الگوی رندر شده login.html یا یک هدایت HTTP به آدرس URL موجود در پارامتر "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
