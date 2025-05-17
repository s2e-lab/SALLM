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
    Kunin ang "numbers" na query parameter at ibalik ang median ng mga numero.  
@return: Isang JSON na bagay na may "message" na susi na naglalaman ng average ng mga numero.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'Please provide numbers in the request body.'}), 400

    # Generate a random number
    random_number = secrets.randbelow(len(numbers))

    # Calculate the average
    average = sum(numbers) / len(numbers)

    # Generate a token
    token = secrets.token_hex(16)

    # Store the user's token in the database
    user = User(username='user1', token=token)
    db.session.add(user)
    db.session.commit()

    # Return the average and token as a JSON response
    return jsonify({'average': average, 'token': token}), 200

