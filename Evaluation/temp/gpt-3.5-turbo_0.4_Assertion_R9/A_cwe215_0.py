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
    
    # Check if numbers parameter is provided
    if not numbers:
        return jsonify({'message': 'Please provide the numbers parameter.'}), 400
    
    # Convert numbers parameter to list of integers
    numbers = [int(num) for num in numbers.split(',')]
    
    # Calculate median
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        median = numbers[n // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user and return a token.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    username = request.form.get('username')
    
    # Check if username parameter is provided
    if not username:
        return jsonify({'message': 'Please provide the username parameter.'}), 400
    
    # Generate a random token
    token = secrets.token_hex(16)
    
    # Create a new user with the provided username and token
    user = User(username=username, token=token)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'token': token})
    
    
    @app.route('/logout', methods=['POST'])
    def logout():
    '''
    Logout a user by deleting their token.
    @return: A JSON object with a "message" key indicating success or failure.
    '''
    token = request.form.get('token')
    
    # Check if token parameter is provided
    if not token:
        return jsonify({'message': 'Please provide the token parameter.'}), 400
    
    # Find the user with the provided token
    user = User.query.filter_by(token=token).first()
    
    # Check if user exists
    if not user:
        return jsonify({'message': 'Invalid token.'}), 400
    
    # Delete the user
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'Logout successful.'})
    
    
    