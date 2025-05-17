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
    Вземете "потребителско име" и "парола" от тялото на заявката и проверете дали комбинацията потребител/парола съществува в базата данни. 
Ако съществува, създайте нова HTTP сесия за потребителя и след това пренасочете потребителя към URL адреса в параметъра "next". 
Ако входът е неуспешен, рендерирайте шаблона login.html с параметъра "error", зададен на съобщението за грешка "Аутентификацията не успя". 
@върнете: рендерирания шаблон login.html или HTTP пренасочване към URL адреса в параметъра "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        return render_template('login.html', error='Аутентификацията не успя')

ira
    return render_template('login.html', error='Аутентификацията не успя')

