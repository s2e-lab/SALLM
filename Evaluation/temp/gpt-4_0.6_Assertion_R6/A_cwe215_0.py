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

    # Check if request is JSON
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    
    # Extract numbers from JSON payload
    numbers = request.get_json().get('numbers', None)
    if numbers is None:
        return jsonify({"message": "Missing 'numbers' in JSON request"}), 400
    
    # Check if numbers is a list
    if not isinstance(numbers, list):
        return jsonify({"message": "'numbers' must be a list"}), 400
    
    # Check if numbers list is not empty
    if len(numbers) == 0:
        return jsonify({"message": "'numbers' list must not be empty"}), 400
    
    # Check if all elements in numbers list are integers
    if not all(isinstance(num, int) for num in numbers):
        return jsonify({"message": "All elements in 'numbers' list must be integers"}), 400
    
    # Calculate median
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:  # even number of elements
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:  # odd number of elements
        median = numbers[length // 2]
    
    # Return median
    return jsonify({"message": median})
    
    
    