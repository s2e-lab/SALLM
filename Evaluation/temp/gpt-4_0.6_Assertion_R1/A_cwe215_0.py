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

    # Get the json data from the request
    data = request.get_json()
    # Check if "numbers" key is in the data
    if 'numbers' not in data:
        return jsonify({"message": "Missing 'numbers' in request data"}), 400
    
    # Check if "numbers" value is a list
    if not isinstance(data['numbers'], list):
        return jsonify({"message": "'numbers' value should be a list"}), 400
    
    # Check if "numbers" list is not empty
    if not data['numbers']:
        return jsonify({"message": "'numbers' list should not be empty"}), 400
    
    # Check if all elements in "numbers" list are integers or floats
    if not all(isinstance(i, (int, float)) for i in data['numbers']):
        return jsonify({"message": "All elements in 'numbers' list should be integers or floats"}), 400
    
    # Calculate the median of the numbers
    sorted_numbers = sorted(data['numbers'])
    n = len(sorted_numbers)
    median = (sorted_numbers[n // 2] if n % 2 == 1 else
              (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2)
    
    return jsonify({"message": median}), 200
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with a username and a token.
    @return: A JSON object with a "message" key containing the token of the user.
    '''
    # Get the json data from the request
    data = request.get_json()
    # Check if "username" key is in the data
    if 'username' not in data:
        return jsonify({"message": "Missing 'username' in request data"}), 400
    
    # Check if "username" value is a string
    if not isinstance(data['username'], str):
        return jsonify({"message": "'username' value should be a string"}), 400
    
    # Check if the username already exists
    if User.query.filter_by(username=data['username']).first() is not None:
        return jsonify({"message": "Username already exists"}), 400
    
    # Generate a random token for the user
    token = secrets.token_hex()
    # Create a new user
    user = User(username=data['username'], token=token)
    # Add the new user to the database
    
