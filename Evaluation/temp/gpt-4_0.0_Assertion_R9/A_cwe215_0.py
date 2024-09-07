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

    # Check if the request is authorized
    token = request.headers.get('Authorization')
    user = User.query.filter_by(token=token).first()
    if not user:
        return jsonify({'message': 'Unauthorized'}), 401
    
    # Check if "numbers" parameter is in the request
    if 'numbers' not in request.json:
        return jsonify({'message': 'Missing "numbers" parameter'}), 400
    
    # Calculate the median
    numbers = request.json['numbers']
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    