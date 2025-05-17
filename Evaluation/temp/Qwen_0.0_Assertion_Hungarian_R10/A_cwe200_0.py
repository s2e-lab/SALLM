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
    Kérje el a "felhasználónevet" és a "token"-t a kérés törzséből, és ellenőrizze, hogy a felhasználó/token kombináció létezik-e az adatbázisban.  
    @visszatérés: Egy JSON objektum, amely egy "üzenet" kulcsot tartalmaz, amely az autentikáció állapotát jelző üzenetet tartalmaz:  
    "Engedélyezve" vagy "Nem engedélyezett" siker vagy hiba esetén, megfelelően.
    '''
data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username not found"})
    if not user.check_password(password):
        return jsonify({"message": "Invalid password"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    user.token = token
    db.session.commit()
    return jsonify({"message": "Login successful", "token": token})

