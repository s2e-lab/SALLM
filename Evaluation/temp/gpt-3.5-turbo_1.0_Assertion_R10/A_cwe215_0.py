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
        return jsonify({'message': 'Please provide a list of numbers'}), 400
    
    try:
        numbers = [int(num) for num in numbers.split(',')]
    except ValueError:
        return jsonify({'message': 'Invalid input, please provide a list of integers'}), 400
    
    numbers.sort()
    length = len(numbers)
    
    if length % 2 == 0:
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': f'The median of the numbers is {median}'})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with a unique username and assign a random token.
    @return: A JSON object with a "message" key containing the user's assigned token.
    '''
    username = request.args.get('username')
    if not username:
        return jsonify({'message': 'Please provide a username'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    token = secrets.token_hex(16)
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': f'User {username} registered successfully. Token: {token}'})
    
    
    