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

    # Extract the numbers from the json request
    numbers = request.get_json(force=True).get('numbers')
    
    # Check if numbers is not None and is not an empty list
    if numbers and len(numbers) > 0:
        # sort the list
        numbers.sort()
        # calculate the median
        if len(numbers) % 2 == 0:  # even number of elements
            median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
        else:  # odd number of elements
            median = numbers[len(numbers) // 2]
    
        # return the result
        return jsonify({'message': median})
    
    # if numbers is None or an empty list return error message
    return jsonify({'error': 'Invalid input'})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "token" key containing the token of the newly created user.
    '''
    # Extract the username from the json request
    username = request.get_json(force=True).get('username')
    
    # Check if the username is not None and is not an empty string
    if username and len(username.strip()) > 0:
        # Check if the user already exists
        user = User.query.get(username)
        if user:
            return jsonify({'error': 'User already exists'})
    
        # Create a new user
        token = secrets.token_hex()
        new_user = User(username=username, token=token)
        db.session.add(new_user)
        db.session.commit()
    
        # return the result
        return jsonify({'token': token})
    
    # if username is None or an empty string return error message
    return jsonify({'error': 'Invalid username'})
    
    
    