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

    numbers = request.json.get('numbers')
    
    if not numbers or len(numbers) == 0:
        return jsonify({'message': 'No numbers provided'})
    
    numbers.sort()
    length = len(numbers)
    
    # If the list has an even number of elements, get the median by averaging the two middle elements
    if length % 2 == 0:
        median = sum(numbers[length // 2 - 1:length // 2 + 1]) / 2
    # If the list has an odd number of elements, the median is the middle number
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    @app.before_first_request
    def create_tables():
    db.create_all()
    
    
    