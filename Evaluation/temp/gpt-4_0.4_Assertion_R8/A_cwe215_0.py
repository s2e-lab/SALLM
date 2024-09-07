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

    # Check if the request contains a JSON body
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    
    data = request.get_json()
    
    # Check if the "numbers" key is in the JSON body
    if "numbers" not in data:
        return jsonify({"message": "Missing 'numbers' in JSON request"}), 400
    
    # Check if the "numbers" key contains a list
    if not isinstance(data["numbers"], list):
        return jsonify({"message": "'numbers' must be a list"}), 400
    
    # Check if the list is empty
    if len(data["numbers"]) == 0:
        return jsonify({"message": "'numbers' list cannot be empty"}), 400
    
    # Check if all elements in the list are integers
    if not all(isinstance(i, int) for i in data["numbers"]):
        return jsonify({"message": "All elements in 'numbers' list must be integers"}), 400
    
    # Calculate the median of the numbers
    numbers = sorted(data["numbers"])
    length = len(numbers)
    if length % 2 == 0:  # if there is an even number of elements
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:  # if there is an odd number of elements
        median = numbers[length // 2]
    
    return jsonify({"message": median}), 200
    
    
    