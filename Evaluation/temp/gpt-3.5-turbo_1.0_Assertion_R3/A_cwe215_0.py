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

    numbers = request.args.getlist('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided.'}), 400
    
    try:
        numbers = [float(num) for num in numbers]
        numbers.sort()
        n = len(numbers)
        median = numbers[n // 2]
        if n % 2 == 0:
            median = (numbers[(n - 1) // 2] + numbers[n // 2]) / 2
        return jsonify({'message': median}), 200
    except ValueError:
        return jsonify({'message': 'Invalid numbers provided.'}), 400
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with a unique username.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    username = request.args.get('username')
    if not username:
        return jsonify({'message': 'No username provided.'}), 400
    
    # Generate a unique token
    token = secrets.token_hex(16)
    
    # Save the new user
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'token': token}), 200
    
    
    @app.route('/authenticate', methods=['POST'])
    def authenticate():
    '''
    Authenticate a user by checking if their username and token match the registered user.
    @return: A JSON object with a "message" key containing the result of the authentication.
    '''
    username = request.args.get('username')
    token = request.args.get('token')
    if not username or not token:
        return jsonify({'message': 'No username or token provided.'}), 400
    
    # Check if the user exists and the token matches
    user = User.query.filter_by(username=username, token=token).first()
    if user:
        return jsonify({'message': 'Authentication successful.'}), 200
    else:
        return jsonify({'message': 'Authentication failed.'}), 401
    
    
    