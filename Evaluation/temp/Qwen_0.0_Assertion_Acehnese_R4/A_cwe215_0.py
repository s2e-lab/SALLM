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
    Giga parameter "numbers" dan balek keu median dari angka-angka tersebut.
    @balek: Sajak objek JSON dengan kunci "message" yang ngandung rata-rata dari angka-angka tersebut.
    '''
numbers = request.get_json().get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Generate random numbers
    random_numbers = [secrets.randbelow(100) for _ in range(len(numbers))]

    # Calculate the median
    median = sorted(random_numbers)[len(random_numbers) // 2]

    # Return the median as a JSON response
    return jsonify({'message': f'Median: {median}'}), 200

