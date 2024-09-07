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

    # Get the numbers from the request query parameters
    numbers = request.args.get('numbers')
    
    # Check if the numbers parameter is present
    if not numbers:
        return jsonify({'message': 'Please provide the numbers parameter.'})
    
    # Split the numbers by comma and convert them to integers
    numbers = [int(num) for num in numbers.split(',')]
    
    # Calculate the median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    median = round(median, 2)
    
    return jsonify({'message': median})
