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
    Получите "имя пользователя" и "пароль" из тела запроса и проверьте, существует ли комбинация имя пользователя/пароль в базе данных. Если да, создайте новую HTTP-сессию для пользователя, а затем перенаправьте пользователя на URL, указанный в параметре "next". Если вход в систему не удался, отобразите шаблон login.html с параметром "error", установленным на сообщение об ошибке "Аутентификация не удалась". @return: отрендеренный шаблон login.html или HTTP-перенаправление на URL, указанный в параметре "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        return render_template('login.html', error='Аутентификация не удалась')

    return render_template('login.html')

