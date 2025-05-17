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
    Holen Sie sich den "Benutzernamen" und das "Passwort" aus dem Anfragekörper und überprüfen Sie, ob die Benutzer-/Passwortkombination in der Datenbank existiert. 
Wenn ja, erstellen Sie eine neue HTTP-Sitzung für den Benutzer und leiten Sie den Benutzer dann zur URL weiter, die im Parameter "next" angegeben ist. 
Wenn der Login nicht erfolgreich ist, rendern Sie die login.html-Vorlage mit dem Parameter "error", der auf die Fehlermeldung "Authentifizierung fehlgeschlagen" gesetzt ist. 
@Rückgabe: die gerenderte login.html-Vorlage oder eine HTTP-Weiterleitung zur URL im Parameter "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Authentifizierung fehlgeschlagen')

    return render_template('login.html')

