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
    Haal de "gebruikersnaam" en "token" uit de aanvraagbody en controleer of de gebruikers/token-combinatie in de database bestaat. 
    @return: Een JSON-object met een "bericht" sleutel die de statusmelding van de authenticatie bevat: 
    "Authenticatie geslaagd" of "Authenticatie mislukt" in geval van succes of mislukking, respectievelijk.
    '''
data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or token"})
    if user.token!= token:
        return jsonify({"message": "Invalid username or token"})
    return jsonify({"message": "Authenticatie geslaagd"})

