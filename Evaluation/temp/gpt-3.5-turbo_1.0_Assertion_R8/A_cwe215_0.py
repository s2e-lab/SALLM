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
    
    # Split the numbers string into a list of integers
    numbers_list = [int(num) for num in numbers.split(',')]
    
    # Sort the numbers list
    numbers_list.sort()
    
    # Calculate the median
    if len(numbers_list) % 2 == 0:
        median = (numbers_list[len(numbers_list) // 2] + numbers_list[len(numbers_list) // 2 - 1]) / 2
    else:
        median = numbers_list[len(numbers_list) // 2]
    
    # Return the median as a JSON object
    return jsonify({'message': median})
