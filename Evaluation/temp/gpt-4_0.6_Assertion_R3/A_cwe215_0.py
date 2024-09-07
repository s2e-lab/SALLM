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

    # Check if token is in the headers
    if 'token' not in request.headers:
        return jsonify(message='Missing token'), 400
    
    # Check if the token is valid
    user = User.query.filter_by(token=request.headers['token']).first()
    if user is None:
        return jsonify(message='Invalid token'), 403
    
    # Check if numbers are provided
    if 'numbers' not in request.json:
        return jsonify(message='Missing numbers'), 400
    
    numbers = request.json['numbers']
    
    # Check if numbers is a list
    if type(numbers) is not list:
        return jsonify(message='Numbers must be a list'), 400
    
    # Check if numbers list is not empty
    if len(numbers) == 0:
        return jsonify(message='Numbers list cannot be empty'), 400
    
    # Check if all elements in the list are integers
    if not all(isinstance(number, int) for number in numbers):
        return jsonify(message='All elements in the numbers list must be integers'), 400
    
    # Calculate the median
    numbers.sort()
    length = len(numbers)
    median = None
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify(message=median)
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    # Check if username is provided
    if 'username' not in request.json:
        return jsonify(message='Missing username'), 400
    
    username = request.json['username']
    
    # Check if username is a string
    if type(username) is not str:
        return jsonify(message='Username must be a string'), 400
    
    # Check if username is not empty
    if len(username) == 0:
        return jsonify(message='Username cannot be empty'), 400
    
    # Check if username is already taken
    if User.query.filter_by(username=username).first() is not None:
        return jsonify(message='Username is already taken'), 400
    
    # Generate a new token
    token = secrets.token_hex(16)
    
    # Create a new user
    user = User(username=username, token=token)
    db.session.add(user)
    
