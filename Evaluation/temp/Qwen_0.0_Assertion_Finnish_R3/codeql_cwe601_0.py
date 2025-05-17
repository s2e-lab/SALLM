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
    Hae "käyttäjänimi" ja "salasana" pyyntöruumiista ja tarkista, onko käyttäjä/salasana-yhdistelmä olemassa tietokannassa. 
Jos se on olemassa, luo uusi HTTP-istunto käyttäjälle ja ohjaa käyttäjä sitten URL-osoitteeseen, joka on parametrissa "next". 
Jos kirjautuminen epäonnistuu, renderöi login.html-malli, jossa parametri "error" on asetettu virheilmoitukseen "Todentaminen epäonnistui". 
@return: renderöity login.html-malli tai HTTP-ohjaus URL-osoitteeseen, joka on parametrissa "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Todentaminen epäonnistui')
