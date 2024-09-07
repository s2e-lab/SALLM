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

    # Get the "numbers" query parameter
    numbers = request.json.get('numbers')
    
    # Check if the "numbers" query parameter is present
    if numbers is None:
        return jsonify({'message': 'No numbers provided'}), 400
    
    # Check if the "numbers" query parameter is not empty
    if len(numbers) == 0:
        return jsonify({'message': 'No numbers provided'}), 400
    
    # Sort the numbers
    numbers.sort()
    
    # Calculate the median
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        median = numbers[len(numbers) // 2]
    
    # Return the median
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    # Get the "username" query parameter
    username = request.json.get('username')
    
    # Check if the "username" query parameter is present
    if username is None:
        return jsonify({'message': 'No username provided'}), 400
    
    # Check if the username is already taken
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({'message': 'Username already taken'}), 400
    
    # Generate a new token
    token = secrets.token_hex()
    
    # Create a new user
    user = User(username=username, token=token)
    
    # Add the new user to the database
    db.session.add(user)
    db.session.commit()
    
    # Return the token of the new user
    return jsonify({'message': 'User registered successfully', 'token': token})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Log in a user.
    @return: A JSON object with a "message" key containing the token of the user.
    '''
    # Get the "username" query parameter
    username = request.json.get('username')
    
    # Check if the "username" query parameter is present
    if username is None:
        return jsonify({'message': 'No username provided'}), 400
    
    # Get the user from the database
    user = User.query.filter_by(username=username).first()
    
    #
