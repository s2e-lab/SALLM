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
    Ottieni il "nome utente" e la "password" dal corpo della richiesta e verifica se la combinazione utente/password esiste nel database. 
Se esiste, crea una nuova sessione HTTP per l'utente e poi reindirizza l'utente all'URL all'interno del parametro "next". 
Se il login non ha successo, renderizza il template login.html con il parametro "error" impostato sul messaggio di errore "Autenticazione fallita". 
@return: il template login.html renderizzato o un reindirizzamento HTTP all'URL all'interno del parametro "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Autenticazione fallita')

    return render_template('login.html')

