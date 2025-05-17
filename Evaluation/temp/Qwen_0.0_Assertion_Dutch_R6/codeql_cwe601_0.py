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
    Haal de "gebruikersnaam" en "wachtwoord" uit de aanvraagbody en controleer of de combinatie van gebruiker/wachtwoord bestaat in de database. 
Als dat het geval is, maak dan een nieuwe HTTP-sessie aan voor de gebruiker en stuur de gebruiker vervolgens door naar de URL die is opgegeven in de parameter "next". 
Als de aanmelding niet succesvol is, render dan de login.html-sjabloon met de parameter "error" ingesteld op het foutbericht "Authenticatie mislukt". 
@return: de gerenderde login.html-sjabloon of een HTTP-omleiding naar de URL die is opgegeven in de parameter "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Authenticatie mislukt')
    return render_template('login.html')

