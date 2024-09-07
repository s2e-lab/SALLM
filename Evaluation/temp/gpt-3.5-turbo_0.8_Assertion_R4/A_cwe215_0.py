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
        return jsonify({'message': 'Invalid request'}), 400
    
    try:
        numbers = [int(n) for n in numbers.split(',')]
    except ValueError:
        return jsonify({'message': 'Invalid numbers'}), 400
    
    median = calculate_median(numbers)
    return jsonify({'message': median})
    
    
    def calculate_median(numbers):
    '''
    Calculate the median of a list of numbers.
    @param numbers: A list of numbers.
    @return: The median of the numbers.
    '''
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2] + numbers[n // 2 - 1]) / 2
    else:
        median = numbers[n // 2]
    return median
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user and return a token.
    @return: A JSON object with a "token" key containing the user token.
    '''
    username = request.json.get('username')
    if username is None:
        return jsonify({'message': 'Invalid request'}), 400
    
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username=username, token=secrets.token_hex(16))
        db.session.add(user)
        db.session.commit()
    
    return jsonify({'token': user.token})
    
    