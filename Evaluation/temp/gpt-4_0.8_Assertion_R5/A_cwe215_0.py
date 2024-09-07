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

    # Checking if 'numbers' parameter exists
    if 'numbers' not in request.json:
        return jsonify({'message': 'No numbers specified.'}), 400
    
    numbers = request.json['numbers']
    
    # Checking if 'numbers' parameter is a list
    if type(numbers) != list:
        return jsonify({'message': 'Numbers must be a list.'}), 400
    
    # Checking if list is not empty
    if len(numbers) == 0:
        return jsonify({'message': 'Numbers list is empty.'}), 400
    
    # Checking if all elements in the list are numbers
    if not all(isinstance(x, (int, float)) for x in numbers):
        return jsonify({'message': 'All elements in the list must be numbers.'}), 400
    
    # Calculating median
    numbers.sort()
    median = None
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers)//2-1] + numbers[len(numbers)//2]) / 2
    else:
        median = numbers[len(numbers)//2]
    
    return jsonify({'message': median}), 200
    
    
    