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

    # Get the "numbers" parameter from the request
    numbers = request.json.get('numbers', None)
    
    # Check if the "numbers" parameter is not None and is a list
    if numbers is None or not isinstance(numbers, list):
        return jsonify({'message': 'Invalid input.'}), 400
    
    # Check if the "numbers" list is not empty
    if not numbers:
        return jsonify({'message': 'No input numbers.'}), 400
    
    # Check if all elements in the "numbers" list are integers
    for num in numbers:
        if not isinstance(num, int):
            return jsonify({'message': 'Input contains non-integer.'}), 400
    
    # Calculate the median of the numbers
    numbers.sort()
    length = len(numbers)
    median = None
    if length % 2 == 0:  # even number of elements
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:  # odd number of elements
        median = numbers[length // 2]
    
    return jsonify({'message': 'Median is {}'.format(median)})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    # Get the "username" parameter from the request
    username = request.json.get('username', None)
    
    # Check if the "username" parameter is not None and is a string
    if username is None or not isinstance(username, str):
        return jsonify({'message': 'Invalid input.'}), 400
    
    # Check if a user with the same username already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already taken.'}), 400
    
    # Create a new user with a random token
    token = secrets.token_hex(16)
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'Registration successful.', 'token': token})
    
    
    