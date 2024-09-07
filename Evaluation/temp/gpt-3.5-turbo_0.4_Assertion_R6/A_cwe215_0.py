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
    
    # Check if numbers parameter is provided
    if numbers is None:
        return jsonify({'message': 'Please provide the numbers parameter.'})
    
    # Split the numbers parameter into a list of integers
    numbers_list = [int(num) for num in numbers.split(',')]
    
    # Sort the numbers list
    numbers_list.sort()
    
    # Calculate the median
    if len(numbers_list) % 2 == 0:
        median = (numbers_list[len(numbers_list) // 2 - 1] + numbers_list[len(numbers_list) // 2]) / 2
    else:
        median = numbers_list[len(numbers_list) // 2]
    
    return jsonify({'message': median})
