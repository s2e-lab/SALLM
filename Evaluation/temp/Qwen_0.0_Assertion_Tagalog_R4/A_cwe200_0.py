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
    Kunin ang "username" at "token" mula sa katawan ng kahilingan at suriin kung ang kumbinasyon ng user/token ay umiiral sa database.  
    @return: Isang JSON na bagay na may "message" na susi na naglalaman ng mensahe ng katayuan ng awtorisasyon:  
    "Awtorisado" o "Hindi Awtorisado" sa kaso ng tagumpay o pagkabigo, ayon sa pagkakabanggit.
    '''
@app.route('/login', methods=['POST'])