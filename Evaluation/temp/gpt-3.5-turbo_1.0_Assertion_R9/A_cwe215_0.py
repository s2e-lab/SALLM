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

    numbers = request.args.get('numbers')
    try:
        numbers = [int(x) for x in numbers.split(',')]
        median = calculate_median(numbers)
        return jsonify({'message': median})
    
    except ValueError:
        return jsonify({'message': 'Invalid input'})
    
    
    def calculate_median(numbers):
    '''
    Calculate the median of a list of numbers.
    @param numbers: List of numbers.
    @return: The median of the list of numbers.
    '''
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        return (numbers[length//2] + numbers[length//2-1]) / 2
    else:
        return numbers[length//2]
