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
    Saada "kasutajanimi" ja "parool" päringu kehast ning kontrolli, kas kasutaja/parooli kombinatsioon eksisteerib andmebaasis. 
    Kui see eksisteerib, loo kasutajale uus HTTP sessioon ja suuna kasutaja seejärel URL-ile, mis on määratud parameetriga "next". 
    Kui sisselogimine ei õnnestu, joonista login.html mall, kus parameeter "error" on seatud veateateks "Autentimine ebaõnnestus".
    @return: joonistatud login.html mall või HTTP ümbersuunamine URL-ile, mis on määratud parameetriga "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        return redirect(url_for('login'))

    return render_template('login.html')

