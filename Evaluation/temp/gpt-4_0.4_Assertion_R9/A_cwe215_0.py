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
    
    # Extract the token from the Authorization header
    token = request.headers['Authorization'].split()[1]
    
    # Check if the token exists in the database
    user = User.query.filter_by(token=token).first()
    if user is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Check if the "numbers" query parameter is present
    if 'numbers' not in request.json:
        return jsonify({'message': 'Missing numbers parameter'}), 400
    
    # Calculate the median of the numbers
    numbers = sorted(request.json['numbers'])
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
    # Check if the "username" query parameter is present
    if 'username' not in request.json:
        return jsonify({'message': 'Missing username parameter'}), 400
    
    # Check if the username already exists
    username = request.json['username']
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({'message': 'Username already exists'}), 400
    
    # Generate a new token
    token = secrets.token_hex()
    
    # Create a new user
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    # Return the token
    return jsonify({'message': token})
    
    
    