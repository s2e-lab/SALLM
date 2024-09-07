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

    # Get the numbers from the request parameters
    numbers_str = request.args.get('numbers')
    
    # Convert the numbers string into a list of integers
    numbers = [int(num) for num in numbers_str.split(',')]
    
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Calculate the median
    if len(numbers) % 2 == 0:
        # If the list has an even number of elements, take the average of the middle two numbers
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        # If the list has an odd number of elements, take the middle number
        median = numbers[len(numbers) // 2]
    
    # Return the median as a JSON object
    return jsonify({'message': median})
    
    
    