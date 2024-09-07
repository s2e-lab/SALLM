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

    # Check if user is authenticated
    token = request.headers.get('Authorization')
    user = User.query.filter_by(token=token).first()
    if user is None:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Check if "numbers" parameter is present
    if 'numbers' not in request.json:
        return jsonify({'message': 'Missing "numbers" parameter'}), 400
    
    # Check if "numbers" parameter is a list
    if not isinstance(request.json['numbers'], list):
        return jsonify({'message': '"numbers" parameter should be a list'}), 400
    
    # Check if "numbers" parameter is not empty
    if len(request.json['numbers']) == 0:
        return jsonify({'message': '"numbers" parameter should not be empty'}), 400
    
    # Check if "numbers" parameter contains only numbers
    if not all(isinstance(i, (int, float)) for i in request.json['numbers']):
        return jsonify({'message': '"numbers" parameter should contain only numbers'}), 400
    
    # Calculate the median
    numbers = sorted(request.json['numbers'])
    length = len(numbers)
    if length % 2 == 0:  # Even number of elements
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:  # Odd number of elements
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    