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

    # Get the "numbers" parameter from the request
    numbers = request.args.get('numbers')
    
    # Split the numbers string by commas
    numbers_list = numbers.split(',')
    
    # Convert the numbers from strings to floats
    numbers_list = [float(number) for number in numbers_list]
    
    # Sort the numbers in ascending order
    numbers_list.sort()
    
    # Calculate the median of the numbers
    n = len(numbers_list)
    if n % 2 == 0:
        median = (numbers_list[n//2 - 1] + numbers_list[n//2]) / 2
    else:
        median = numbers_list[n//2]
    
    # Return the median as a JSON response
    return jsonify({'message': median})
