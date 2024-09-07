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

    # Check if "numbers" parameter exists in the request's body
    if "numbers" not in request.json:
        return jsonify({"message": "Missing 'numbers' in request"}), 400
    
    numbers = request.json["numbers"]
    
    # Check if "numbers" parameter is a list
    if not isinstance(numbers, list):
        return jsonify({"message": "'numbers' must be a list"}), 400
    
    # Check if "numbers" parameter contains only integers
    if not all(isinstance(n, int) for n in numbers):
        return jsonify({"message": "'numbers' must contain only integers"}), 400
    
    # Calculate median of the numbers
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    
    return jsonify({"message": median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with a unique username and generate a token for the user.
    @return: A JSON object with a "token" key containing the token of the user.
    '''
    username = request.json.get('username')
    
    # Check if username is provided
    if not username:
        return jsonify({"message": "Missing 'username' in request"}), 400
    
    user = User.query.filter_by(username=username).first()
    
    # Check if username already exists
    if user:
        return jsonify({"message": "Username already exists"}), 400
    
    # Generate a random token for the user
    token = secrets.token_hex(16)
    
    # Create a new user and save to the database
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"token": new_user.token}), 201
    
    
    # Initialize the database
    @app.before_first_request
    def create_tables():
    db.create_all()
    
    
    