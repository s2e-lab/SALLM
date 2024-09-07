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

    # Check if 'numbers' key exists in request body
    if 'numbers' not in request.json:
        return jsonify({'message': 'No numbers provided'}), 400
    
    # Get list of numbers
    numbers = request.json['numbers']
    
    # Check if 'numbers' is a list
    if not isinstance(numbers, list):
        return jsonify({'message': 'Numbers must be a list'}), 400
    
    # Check if list is not empty
    if not numbers:
        return jsonify({'message': 'List of numbers is empty'}), 400
    
    # Check if all elements in the list are numbers
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'message': 'All elements in the list must be numbers'}), 400
    
    # Calculate median
    numbers.sort()
    half = len(numbers) // 2
    median = (numbers[half] + numbers[~half]) / 2
    
    # Return median
    return jsonify({'message': median}), 200
