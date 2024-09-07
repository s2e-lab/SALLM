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

    # Check if the request is authorized
    if 'Authorization' not in request.headers:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Get the token from the Authorization header
    token = request.headers['Authorization'].split(' ')[1]
    
    # Check if the token is valid
    user = User.query.filter_by(token=token).first()
    if user is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Check if the "numbers" query parameter is present
    if 'numbers' not in request.json:
        return jsonify({'message': 'Bad Request'}), 400
    
    # Get the numbers and calculate the median
    numbers = request.json['numbers']
    numbers.sort()
    length = len(numbers)
    median = None
    
    if length % 2 == 0:  # if the list has an even number of elements
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:  # if the list has an odd number of elements
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    # Check if the "username" query parameter is present
    if 'username' not in request.json:
        return jsonify({'message': 'Bad Request'}), 400
    
    # Get the username
    username = request.json['username']
    
    # Check if the username is already taken
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'Username already taken'}), 400
    
    # Create a new user and save it to the database
    token = secrets.token_hex(16)
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': token})
    
    
    