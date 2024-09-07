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

    data = request.get_json()
    numbers = data['numbers']
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
    @return: A JSON object with a "message" key containing the generated token.
    '''
    username = request.get_json()['username']
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'User already exists'}), 400
    
    user = User(username=username, token=secrets.token_hex(16))
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered', 'token': user.token})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user.
    @return: A JSON object with a "message" key containing the user token.
    '''
    username = request.get_json()['username']
    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify({'message': 'Logged in', 'token': user.token})
    
    