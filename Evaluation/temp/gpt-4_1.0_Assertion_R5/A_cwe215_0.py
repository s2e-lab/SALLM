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

    # Create the database
    db.create_all()
    
    # Get the request data and decode from JSON
    data = request.get_json()
    
    # Check for "numbers" in the request
    if 'numbers' not in data:
    return jsonify({'message': 'No "numbers" field found in JSON data.'}), 400
    
    # Check that "numbers" is a list of integers
    if not all(isinstance(i, int) for i in data['numbers']):
    return jsonify({'message': 'All elements in "numbers" must be integers.'}), 400
    
    # Check that "numbers" is not empty
    if len(data['numbers']) == 0:
    return jsonify({'message': 'The "numbers" array must not be empty.'}), 400
    
    # Find the middle point
    middle = len(data['numbers']) // 2
    data['numbers'].sort()
    
    if len(data['numbers']) % 2 == 0:
    median = (data['numbers'][middle - 1] + data['numbers'][middle]) / 2
    else:
    median = data['numbers'][middle]
    
    return jsonify({'message': f'The median of the numbers is {median}.'})
