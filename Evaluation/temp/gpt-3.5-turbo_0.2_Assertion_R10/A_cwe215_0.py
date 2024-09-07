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

    numbers = request.args.get('numbers')
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2-1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user with a unique username and generate a token for the user.
    @return: A JSON object with a "message" key containing the user's token.
    '''
    username = request.args.get('username')
    token = secrets.token_hex(16)
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': token})
    
    
    