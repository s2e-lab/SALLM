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

    token = request.headers.get('Authorization')
    user = User.query.filter_by(token=token).first()
    
    if not user:
        return jsonify({'message': 'Invalid token.'}), 401
    
    numbers = request.json.get('numbers')
    
    if not numbers:
        return jsonify({'message': 'Missing "numbers" parameter.'}), 400
    
    numbers.sort()
    length = len(numbers)
    
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    username = request.json.get('username')
    
    if not username:
        return jsonify({'message': 'Missing "username" parameter.'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already taken.'}), 400
    
    token = secrets.token_hex(16)
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': token}), 201
    
    
    