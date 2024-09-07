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
    
    n = len(numbers)
    median = numbers[n//2] if n % 2 != 0 else (numbers[n//2-1] + numbers[n//2]) / 2.0
  
    return jsonify({'message': f'Median is {median}'})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Authenticate the user and return a unique token.
    If the user exists, return the existing token.
    If the user does not exist, create a new entry and return a new token.
    '''
    data = request.get_json()
    username = data['username']
    
    user = User.query.filter_by(username=username).first()  
    
    if user is None:
        # Create a new user
        token = secrets.token_hex()
        new_user = User(username=username, token=token)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'token': token})
    
    else:
        # Return existing user's token
        return jsonify({'token': user.token})
    
    
    