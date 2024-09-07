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
    if not numbers:
        return jsonify({'message': 'Please provide numbers.'}), 400
    
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    numbers.sort()
    
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median = numbers[len(numbers) // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user and generate a token for authentication.
    @return: A JSON object with a "token" key containing the generated token.
    '''
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Please provide username and password.'}), 400
    
    # Check if user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username or password.'}), 401
    
    # Check if password is correct
    if password != user.password:
        return jsonify({'message': 'Invalid username or password.'}), 401
    
    # Generate token
    token = secrets.token_hex(16)
    user.token = token
    db.session.commit()
    
    return jsonify({'token': token})
    
    
    @app.route('/logout', methods=['POST'])
    def logout():
    '''
    Logout a user by removing their token.
    @return: A JSON object with a "message" key indicating successful logout.
    '''
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({'message': 'Please provide a token.'}), 400
    
    # Check if token is valid
    user = User.query.filter_by(token=token).first()
    if not user:
        return jsonify({'message': 'Invalid token.'}), 401
    
    # Remove token
    user.token = None
    db.session.commit()
    
    return jsonify({'message': 'Logout successful.'})
    
    
    