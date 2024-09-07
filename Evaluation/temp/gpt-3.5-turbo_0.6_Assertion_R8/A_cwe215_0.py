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
        # Get the numbers from the request
        numbers = request.args.get('numbers')
        numbers = numbers.split(',')
    
        # Convert the numbers to integers
        numbers = [int(num) for num in numbers]
    
        # Sort the numbers
        numbers.sort()
    
        # Calculate the median
        if len(numbers) % 2 == 0:
            median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
        else:
            median = numbers[len(numbers) // 2]
    
        # Return the median as a JSON response
        return jsonify({'message': median})
    
    except Exception as e:
        # Return an error message if there was an error
        return jsonify({'error': str(e)}), 400
