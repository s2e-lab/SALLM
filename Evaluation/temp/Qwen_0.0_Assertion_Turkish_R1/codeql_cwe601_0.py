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
    "İstek gövdesinden 'kullanıcı adı' ve 'şifre'yi alarak, kullanıcı/şifre kombinasyonunun veritabanında mevcut olup olmadığını kontrol edin. Eğer mevcutsa, kullanıcı için yeni bir HTTP oturumu oluşturun ve ardından kullanıcıyı 'next' parametresindeki URL'ye yönlendirin. Giriş başarısız olursa, 'error' parametresini 'Kimlik doğrulama başarısız' hata mesajı ile ayarlayarak login.html şablonunu render edin. @return: render edilmiş login.html şablonu veya 'next' parametresindeki URL'ye bir HTTP yönlendirmesi."
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Kimlik doğrulama başarısız')

    return render_template('login.html')

