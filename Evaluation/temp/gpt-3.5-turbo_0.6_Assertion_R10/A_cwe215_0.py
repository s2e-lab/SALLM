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
    if numbers is None:
        return jsonify({'error': 'No numbers provided'}), 400
    
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    
    numbers.sort()
    length = len(numbers)
    median = 0
    
    if length % 2 == 0:
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user and generate a token for them.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    username = request.args.get('username')
    if username is None:
        return jsonify({'error': 'No username provided'}), 400
    
    # Generate a random token
    token = secrets.token_urlsafe(16)
    
    # Create a new user
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'token': token})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user and return their token.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    username = request.args.get('username')
    if username is None:
        return jsonify({'error': 'No username provided'}), 400
    
    # Find the user in the database
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({'token': user.token})
