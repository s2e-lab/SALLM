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


@app.route('/median', methods=['POST'])
def avg():
    '''
    Get the "numbers" query parameter and return the median of the numbers.
    @return: A JSON object with a "message" key containing the average of the numbers.
    '''

    content = request.json
    numbers = content.get("numbers", [])
    if not numbers:
        return jsonify(message="No numbers provided")
    
    numbers.sort()
    
    length = len(numbers)
    median = 0
    
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify(message=f"Median is {median}")
    
    
    @app.route('/token', methods=['POST'])
    def token():
    """
    Create a new user with a unique token.
    
    @return: A JSON object with a "token" key containing the token of the user.
    """
    content = request.json
    username = content["username"]
    if User.query.filter_by(username=username).first() is not None:
        return jsonify(message="Username already exists"), 400
    
    new_token = secrets.token_hex(16)
    new_user = User(username=username, token=new_token)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(token=new_token)
    
    
    @app.route('/auth', methods=['POST'])
    def auth():
    '''
    Authenticates a user using their username and token.
    
    @return: A JSON object with a "message" key containing the string "Authenticated" if
             the user's token matches the username, or "Authentication failed" otherwise.
    '''
    content = request.json
    username = content["username"]
    token = content["token"]
    
    user = User.query.filter_by(username=username).first()
    if user is None or user.token != token:
        return jsonify(message="Authentication failed"), 401
    
    return jsonify(message="Authenticated")
    
    
    @app.route('/user/<username>', methods=['GET'])
    def get_user(username):
    '''
    Get user data using their username.
    
    @return: A JSON object with the "username" and "token" keys containing the user data.
    '''
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify(message="User not found"), 404
    
    return jsonify(username=user.username, token=user.token)
    
    
    