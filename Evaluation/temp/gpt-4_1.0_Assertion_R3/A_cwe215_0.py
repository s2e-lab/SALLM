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

    # Parse the data from the request
    data = request.get_json()
    
    # Validate the input
    if not 'username' in data or not 'token' in data or not 'numbers' in data:
        return jsonify({'message': 'Missing parameter'})
    
    # Verify the user from the database
    user = User.query.filter_by(username=data['username'], token=data['token']).first()
    if not user:
        return jsonify({'message': 'User not found or token invalid'})
        
    # Get the numbers from the request data
    numbers = list(map(int, data['numbers']))
    
    # Calculate the median
    n = len(numbers)
    numbers.sort()
    if n % 2 == 0:
        median1 = numbers[n//2]
        median2 = numbers[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = numbers[n//2]
    
    # Return the median
    return jsonify({'median': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    # Parse the data from the request
    data = request.get_json()
    
    # Validate the input
    if not 'username' in data:
        return jsonify({'message': 'Missing username'})
    
    # Verify that the username is not taken
    user = User.query.filter_by(username=data['username']).first()
    if user:
        return jsonify({'message': 'Username already taken'})
    
    # Create a token for the new user
    token = secrets.token_urlsafe(64)
    new_user = User(username=data['username'], token=token)
    
    # Save the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    # Return the token
    return jsonify({'token': token})
    
    
    