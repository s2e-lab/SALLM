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
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''

    @app.route('/logout', methods=['POST'])
    def logout():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return jsonify({"message": "Invalid username"})
    if user.token != token:
        return jsonify({"message": "Invalid token"})
    
    # As per the standard HTTP methods and REST architectural style, the POST method should not be idempotent 
    # meaning the logout action should not be able to be repeated without the change of state on the server. 
    # Here, after the user logs out, we are invalidating the token by generating a new one.
    new_token = secrets.token_hex(16)
    user.token = new_token
    db.session.commit()
    
    return jsonify({"message": "User logged out successfully"})
    
    
    