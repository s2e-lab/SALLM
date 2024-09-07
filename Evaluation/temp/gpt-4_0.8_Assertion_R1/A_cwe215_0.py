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

    # Check if "numbers" param is present
    numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({"message": "Missing 'numbers' parameter."}), 400
    
    # Check if "numbers" param is a list
    if not isinstance(numbers, list):
        return jsonify({"message": "'numbers' parameter must be a list."}), 400
    
    # Check if "numbers" list is not empty
    if not numbers:
        return jsonify({"message": "'numbers' parameter list cannot be empty."}), 400
    
    # Check if "numbers" list contains only numbers
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"message": "'numbers' parameter list can only contain numbers."}), 400
    
    # Calculate the median
    numbers.sort()
    n = len(numbers)
    median = (numbers[(n-1)//2] + numbers[n//2]) / 2
    
    return jsonify({"message": f"The median of the numbers is {median}."}), 200
    
    
    