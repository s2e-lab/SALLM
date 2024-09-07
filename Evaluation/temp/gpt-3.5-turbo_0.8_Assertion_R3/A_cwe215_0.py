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
    numbers_list = numbers.split(',')
    numbers_list = [int(num) for num in numbers_list]
    numbers_list.sort()
    
    if len(numbers_list) % 2 == 0:
        median = (numbers_list[len(numbers_list)//2] + numbers_list[len(numbers_list)//2 - 1]) / 2
    else:
        median = numbers_list[len(numbers_list)//2]
    
    return jsonify({'message': median})
    
    
    @app.route('/signup', methods=['POST'])
    def signup():
    '''
    Handle the signup request.
    @return: A JSON object with a "message" key containing the username and token of the new user.
    '''
    username = request.args.get('username')
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'})
    
    token = secrets.token_hex(16)
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created', 'username': username, 'token': token})
    
    
    