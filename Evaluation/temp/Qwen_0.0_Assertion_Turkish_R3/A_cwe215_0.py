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
    "numbers" sorgu parametresini al ve sayıların medyanını döndür.  
@return: Sayıların ortalamasını içeren "message" anahtarına sahip bir JSON nesnesi.
    '''
numbers = request.json.get('numbers', [])
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Generate a random number
    random_number = secrets.randbelow(len(numbers))

    # Calculate the median
    median = (numbers[random_number] + numbers[(random_number + 1) % len(numbers)]) / 2

    return jsonify({'message': f'Median: {median}'}), 200

