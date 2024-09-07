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

    # First, we need to make sure all the needed tables are created in our sqlite database
    db.create_all()
    
    # Then, let's get the numbers from the HTTP request
    numbers = request.json.get('numbers', [])
    
    # Let's make sure the numbers are sorted in increasing order
    numbers.sort()
    
    # If there are no numbers, we can't calculate the median
    if len(numbers) == 0:
    return jsonify({'message': 'No numbers provided'}), 400
    
    # Let's calculate the median; if the list of numbers has an odd length, the median is the middle number;
    # if the list has an even length, the median is the average of the two middle numbers
    if len(numbers) % 2 == 1:
    median = numbers[len(numbers) // 2]
    else:
    median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2.0
    
    # Finally, we can return the result
    return jsonify({'message': median})
