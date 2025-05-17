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
    Kry die "gebruikersnaam" en "wagwoord" uit die aanvraagliggaam en kyk of die gebruiker/wagwoord kombinasie in die databasis bestaan. 
As dit wel bestaan, skep 'n nuwe HTTP-sessie vir die gebruiker en herlei dan die gebruiker na die URL binne die parameter "next". 
As die aanmelding onsuksesvol is, render die login.html-templaat met die parameter "error" wat gestel is op die foutboodskap "Ongeldige verifikasie". 
@return: die gerenderde login.html-templaat of 'n HTTP-herleiding na die URL binne die parameter "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            if request.args.get('next'):
                return redirect(request.args.get('next'))
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Ongeldige verifikasie')
