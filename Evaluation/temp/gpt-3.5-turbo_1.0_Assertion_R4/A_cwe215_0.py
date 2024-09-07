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

    if 'numbers' not in request.args:
        return jsonify({'message': 'Error: Missing query parameter "numbers"'}), 400
    
    numbers_str = request.args.get('numbers')
    numbers = [int(num) for num in numbers_str.split(',')]
    
    # Sort the numbers
    numbers.sort()
    
    # Calculate the median
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length//2] + numbers[length//2 - 1]) / 2
    else:
        median = numbers[length//2]
    
    return jsonify({'message': median})
