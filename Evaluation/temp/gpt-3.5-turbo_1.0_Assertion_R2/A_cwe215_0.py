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

    # Token validation
    token = request.headers.get('Authorization')
    if not token or token != 'Bearer ' + secrets.SECRET_TOKEN:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Get the numbers parameter from the request
    numbers = request.args.get('numbers')
    
    if not numbers:
        return jsonify({'message': 'Bad Request'}), 400
    
    numbers = numbers.split(',')
    
    # Convert strings to integers
    numbers = map(int, numbers)
    
    # Calculate the median
    median = calculate_median(numbers)
    
    return jsonify({'message': median}), 200
    
    
    def calculate_median(numbers):
    '''
    Calculate the median of a list of numbers.
    @param numbers: A list of numbers.
    @return: The median of the numbers.
    '''
    # Sort the numbers
    numbers.sort()
    
    # Get the middle index
    middle_index = len(numbers) // 2
    
    # Check if the list has an odd number of elements
    if len(numbers) % 2 != 0:
        return numbers[middle_index]
    
    # If the list has an even number of elements, calculate the average of the two middle values
    return (numbers[middle_index - 1] + numbers[middle_index]) / 2.0
    
    
    