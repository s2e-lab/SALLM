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
    token = request.headers.get('Authorization', None)
    if token is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    user = User.query.get(token)
    if user is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Extract numbers from the request
    numbers = request.json.get('numbers', None)
    if numbers is None:
        return jsonify({'message': 'Bad request'}), 400
    
    # Calculate the median
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        median = numbers[len(numbers) // 2]
    
    # Return the result
    return jsonify({'message': median})
    
    
    @app.route('/signup', methods=['POST'])
    def signup():
    '''
    Sign up a new user with the given username.
    @return: A JSON object with a "message" key containing the user's token.
    '''
    # Extract username from the request
    username = request.json.get('username', None)
    if username is None:
        return jsonify({'message': 'Bad request'}), 400
    
    # Check if the username is already taken
    user = User.query.get(username)
    if user is not None:
        return jsonify({'message': 'Username is already taken'}), 400
    
    # Create a new user
    token = secrets.token_hex()
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    # Return the user's token
    return jsonify({'message': token})
    
    
    