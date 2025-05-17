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
    پارامتر "numbers" را دریافت کرده و میانه اعداد را برگردانید. 
    @return: یک شیء JSON با یک کلید "message" که میانگین اعداد را در بر دارد.
    '''
numbers = request.get_json().get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Generate a random number
    random_number = secrets.randbelow(len(numbers))

    # Calculate the average
    average = sum(numbers) / len(numbers)

    # Return the average as a JSON response
    return jsonify({'message': f'Average: {average}'}), 200

