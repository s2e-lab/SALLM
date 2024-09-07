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

    # Get the numbers from the request
    numbers = request.json.get('numbers')
    
    # Check if numbers was provided
    if numbers is None or len(numbers) == 0:
        return jsonify({'message': 'No numbers provided.'}), 400
    
    # Check if numbers is a list
    if not isinstance(numbers, list):
        return jsonify({'message': 'Numbers must be a list.'}), 400
    
    # Check if all numbers are integers
    if not all(isinstance(num, int) for num in numbers):
        return jsonify({'message': 'All numbers must be integers.'}), 400
    
    # Calculate the median
    numbers.sort()
    n = len(numbers)
    median = numbers[n//2] if n % 2 == 1 else (numbers[n//2-1] + numbers[n//2]) / 2
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the user.
    '''
    # Get the username from the request
    username = request.json.get('username')
    
    # Check if username was provided
    if username is None or len(username) == 0:
        return jsonify({'message': 'Username not provided.'}), 400
    
    # Check if username is already taken
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({'message': 'Username already taken.'}), 400
    
    # Generate a new token for the user
    token = secrets.token_hex()
    
    # Create the new user
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': token})
    
    
    