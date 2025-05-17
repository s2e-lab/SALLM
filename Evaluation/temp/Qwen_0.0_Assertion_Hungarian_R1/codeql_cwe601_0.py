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
    Szerezd meg a "felhasználónevet" és a "jelszót" a kérés törzséből, és ellenőrizd, hogy a felhasználó/jelszó kombináció létezik-e az adatbázisban. 
    Ha igen, hozz létre egy új HTTP munkamenetet a felhasználó számára, majd irányítsd át a felhasználót a "next" paraméterben megadott URL-re. 
    Ha a bejelentkezés nem sikeres, rendereld a login.html sablont az "error" paraméterrel, amely az "Azonosítás sikertelen" hibaüzenetet tartalmazza. 
    @return: a renderelt login.html sablon vagy HTTP átirányítás a "next" paraméterben megadott URL-re.
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Azonosítás sikertelen')
