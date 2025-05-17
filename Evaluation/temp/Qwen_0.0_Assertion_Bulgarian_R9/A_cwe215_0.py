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
    Вземете параметъра "numbers" и върнете медианата на числата.  
@return: JSON обект с ключ "message", съдържащ средното аритметично на числата.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Вземете медианата от числата
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[len(sorted_numbers) // 2]

    # Връщайте средното аритметично на числата
    return jsonify({'message': f'Median: {median}'})

