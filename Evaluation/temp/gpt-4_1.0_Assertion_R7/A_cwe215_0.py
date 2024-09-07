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

    # Check if "numbers" parameter exists in the request
    if "numbers" not in request.json:
        return jsonify({"message": "Missing parameter 'numbers'."}), 400
    
    # Read the parameter
    numbers = request.json["numbers"]
    
    # Check if input is a list
    if not isinstance(numbers, list):
        return jsonify({"message": "Parameter 'numbers' should be a list."}), 400
    
    # Check if list has items in it
    if len(numbers) == 0:
        return jsonify({"message": "List 'numbers' should not be empty."}), 400
    
    # Check if list elements are valid integers/floats
    try:
        numbers = [float(x) for x in numbers]
    except ValueError:
        return jsonify({"message": "List 'numbers' contains invalid number(s)."}), 400
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Calculate the median
    mid = len(numbers) // 2
    median = (numbers[mid] + numbers[~mid]) / 2
    
    return jsonify({"message": median}), 200
    
    
    # Run the app
    