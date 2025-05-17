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
    Holen Sie den "numbers" Abfrageparameter und geben Sie den Median der Zahlen zurück. 
    @return: Ein JSON-Objekt mit einem Schlüssel "message", das den Durchschnitt der Zahlen enthält.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Generate a random number
    random_number = secrets.randbelow(len(numbers))

    # Calculate the median
    median = sum(numbers) / len(numbers)

    # Return the median as a JSON response
    return jsonify({'message': f'Median: {median}'}), 200

