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

    try:
        # Check if "numbers" is in the request body
        if 'numbers' not in request.json:
            return jsonify({'error': 'Missing "numbers" in request body.'}), 400
    
        # Check if "numbers" is a list
        if not isinstance(request.json['numbers'], list):
            return jsonify({'error': '"numbers" should be a list.'}), 400
    
        # Check if "numbers" is an empty list
        if len(request.json['numbers']) == 0:
            return jsonify({'error': '"numbers" list should not be empty.'}), 400
    
        # Check if "numbers" is a list of numbers
        if not all(isinstance(n, (int, float)) for n in request.json['numbers']):
            return jsonify({'error': '"numbers" list should only contain numbers.'}), 400
    
        numbers = sorted(request.json['numbers'])
        length = len(numbers)
    
        # Compute the median
        if length % 2 == 0:  # even number of elements
            median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
        else:  # odd number of elements
            median = numbers[length // 2]
    
        return jsonify({'message': median})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    @app.before_request
    def require_login():
    '''
    Check if the user is authenticated before processing the request.
    '''
    token = request.headers.get('authorization')
    
    if token is None:
        return jsonify({'error': 'Missing authorization token.'}), 401
    
    user = User.query.filter_by(token=token).first()
    
    if user is None:
        return jsonify({'error': 'Invalid authorization token.'}), 401
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    try:
        # Check if "username" is in the request body
        if 'username' not in request.json:
            return jsonify({'error': 'Missing "username" in request body.'}), 400
    
        username = request.json['username']
    
        # Check if the username is already taken
        if User.query.filter_by(username=username).first() is not None:
            return jsonify({'error': 'Username already taken.'}), 400
    
    
