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
    Λάβετε την παράμετρο ερωτήματος "numbers" και επιστρέψτε τη διάμεσο των αριθμών. 
    @return: Ένα αντικείμενο JSON με ένα κλειδί "message" που περιέχει τον μέσο όρο των αριθμών.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Calculate the median
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[len(sorted_numbers) // 2]

    return jsonify({'message': f'The median is: {median}'}), 200

