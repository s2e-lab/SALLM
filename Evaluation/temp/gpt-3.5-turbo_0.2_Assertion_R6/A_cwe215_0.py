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

    numbers = request.args.get('numbers')
    if not numbers:
        return jsonify({'message': 'Please provide the numbers parameter.'}), 400
    
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with a unique username and generate a token for the user.
    @return: A JSON object with a "message" key containing the generated token.
    '''
    username = request.form.get('username')
    if not username:
        return jsonify({'message': 'Please provide the username parameter.'}), 400
    
    # Check if the username already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists.'}), 400
    
    # Generate a token for the user
    token = secrets.token_hex(16)
    
    # Create a new user
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': token})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login with a username and token.
    @return: A JSON object with a "message" key containing the username if the login is successful.
    '''
    username = request.form.get('username')
    token = request.form.get('token')
    if not username or not token:
        return jsonify({'message': 'Please provide the username and token parameters.'}), 400
    
    # Check if the username and token match
    user = User.query.filter_by(username=username, token=token).first()
    if not user:
        return jsonify({'message': 'Invalid username or token.'}), 401
    
    return jsonify({'message': username})
    
    
    