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
    
    # Get the JSON body of the request
    data = request.get_json()
    
    # Check if the "numbers" key is in the JSON body
    if "numbers" not in data:
        return jsonify({"message": "Missing 'numbers' in JSON"}), 400
    
    # Get the list of numbers
    numbers = data["numbers"]
    
    # Check if the list of numbers is not empty
    if not numbers:
        return jsonify({"message": "Empty list of numbers"}), 400
    
    # Check if all elements in the list are numbers
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"message": "All elements in the list must be numbers"}), 400
    
    # Calculate the median of the numbers
    numbers.sort()
    n = len(numbers)
    median = (numbers[n//2] if n % 2 == 1 else (numbers[n//2 - 1] + numbers[n//2]) / 2)
    
    # Return the median
    return jsonify({"message": median}), 200
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    # Check if the request contains a JSON body
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    
    # Get the JSON body of the request
    data = request.get_json()
    
    # Check if the "username" key is in the JSON body
    if "username" not in data:
        return jsonify({"message": "Missing 'username' in JSON"}), 400
    
    # Get the username
    username = data["username"]
    
    # Check if the username is not empty
    if not username:
        return jsonify({"message": "Username cannot be empty"}), 400
    
    # Check if the username is already taken
    if User.query.get(username):
        return jsonify({"message": "Username is already taken"}), 400
    
    # Generate a new token
    token = secrets.token_hex()
    
    # Create a new user
    user = User(username=username, token=token)
    
    # Add the
