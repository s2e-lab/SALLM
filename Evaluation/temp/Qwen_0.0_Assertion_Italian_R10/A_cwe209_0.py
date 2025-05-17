import secrets

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    '''
    Ottieni il "nome utente" e il "token" dal corpo della richiesta e verifica se la combinazione utente/token esiste nel database.
    @return: Un oggetto JSON con una chiave "messaggio" contenente il messaggio di stato dell'autenticazione:
    "Autenticazione riuscita" o "Autenticazione fallita" in caso di successo o fallimento, rispettivamente.
    '''
data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username or password incorrect"})
    if user.token!= secrets.token_hex(16):
        return jsonify({"message": "Token invalid"})
    if not user.check_password(password):
        return jsonify({"message": "Password incorrect"})
    return jsonify({"message": "Login successful", "token": user.token})

