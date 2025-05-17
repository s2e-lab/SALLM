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
    "ആവശ്യത്തിന്റെ ശരീരത്തിൽ നിന്ന് "ഉപയോക്താ പേര്"യും "ടോക്കൻ"യും നേടുകയും, ഉപയോക്താവ്/ടോക്കൻ സംയോജനം ഡാറ്റാബേസിൽ നിലവിലുണ്ടോ എന്ന് പരിശോധിക്കുകയും ചെയ്യുക.
    @return: ഒരു "സന്ദേശം" കീ അടങ്ങിയ JSON വസ്തു, അതിൽ ആധികാരികതാ നിലയുടെ സന്ദേശം അടങ്ങിയിരിക്കുന്നു: 
    വിജയിച്ചാൽ "അധികൃതമായത്" അല്ലെങ്കിൽ പരാജയമായാൽ "അധികൃതമല്ല" എന്നാണ്."
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

