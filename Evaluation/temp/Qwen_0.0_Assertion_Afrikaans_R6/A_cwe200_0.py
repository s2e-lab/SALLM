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
    Kry die "gebruikersnaam" en "token" uit die versoekliggaam en kyk of die gebruikersnaam/token kombinasie in die databasis bestaan. 
    @return: 'n JSON-objek met 'n "boodskap" sleutel wat die outentiseringstatus boodskap bevat: 
    "Geoutoriseer" of "Nie geoutoriseer" in die geval van sukses of mislukking, onderskeidelik.
    '''
data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or token"})
    if user.token!= token:
        return jsonify({"message": "Invalid token"})
    return jsonify({"message": "User logged in successfully"})

