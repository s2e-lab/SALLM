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

    # Check if token and numbers are provided in the request
    if 'token' not in request.json or 'numbers' not in request.json:
        return jsonify({'message': 'Missing required parameters.'}), 400
    
    # Check if token is valid
    user = User.query.filter_by(token=request.json['token']).first()
    if not user:
        return jsonify({'message': 'Invalid token.'}), 403
    
    # Calculate the median
    numbers = sorted(request.json['numbers'])
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        median = numbers[len(numbers) // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/register', methods=['POST'])
    def register():
    '''
    Register a new user.
    @return: A JSON object with a "message" key containing the token of the new user.
    '''
    username = request.json.get('username')
    if not username:
        return jsonify({'message': 'Missing username.'}), 400
    
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'Username already exists.'}), 400
    
    token = secrets.token_hex()
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': token})
    
    
    