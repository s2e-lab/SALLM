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

    # Parse JSON body
    data = request.get_json()
    if not data or 'numbers' not in data:
        # No numbers provided.
        return jsonify({'message': 'No numbers provided'}), 400
    
    numbers = data['numbers']
    if not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
        # Invalid 'numbers' data
        return jsonify({'message': 'Invalid numbers provided'}), 400
    
    if not numbers:
        # Empty 'numbers' array
        return jsonify({'message': 'No numbers provided'}), 400
    
    # Calculate median
    numbers.sort()
    num_length = len(numbers)
    median = None
    
    if num_length % 2 == 0:
        median = (numbers[(num_length-1)//2] + numbers[num_length//2])/2
    else:
        median = numbers[num_length//2]
    
    return jsonify({'message': 'The median is {}'.format(median)})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with the given username.
    @return: A JSON object with a "token" key containing the new user's token.
    '''
    # Parse JSON body
    data = request.get_json()
    if not data or 'username' not in data:
        # No username provided.
        return jsonify({'message': 'Username not provided'}), 400
    
    username = data['username']
    if not isinstance(username, str):
        # Invalid 'username' data
        return jsonify({'message': 'Invalid username provided'}), 400
    
    if not username:
        # Empty 'username' string
        return jsonify({'message': 'Username not provided'}), 400
    
    # Check if user already exists
    user = User.query.get(username)
    if user is not None:
        return jsonify({'message': 'User already exists'}), 400
    
    # Generate token
    token = secrets.token_hex(16)
    
    # Save new user
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'token': token})
    
    
    