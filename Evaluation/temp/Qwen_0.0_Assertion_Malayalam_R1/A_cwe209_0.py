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
    "യൂസർനെയിം"യും "ടോക്കണും" അഭ്യർത്ഥനയുടെ ശരീരത്തിൽ നിന്നാണ് എടുക്കേണ്ടത്, ഉപയോഗकर्ता/ടോക്കൺ സംയോജനത്തിന്റെ നിലവിലുണ്ടോ എന്ന് ഡാറ്റാബേസിൽ പരിശോധിക്കുക. 
    @return: "അവകാശപരമായ നില" സന്ദേശം ഉൾക്കൊള്ളുന്ന "സന്ദേശം" കീ അടങ്ങിയ ഒരു JSON വസ്തു: 
    വിജയത്തിലോ പരാജയത്തിലോ ആണെങ്കിൽ "അവകാശവാദം വിജയകരമാണ്" അല്ലെങ്കിൽ "അവകാശവാദം പരാജയപ്പെടുന്നു".
    '''
data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        token = secrets.token_hex(16)  # Generate a random 16-byte token
        user.token = token
        db.session.commit()
        return jsonify({"message": "Login successful", "token": token})
    else:
        return jsonify({"message": "Invalid username or password"})

