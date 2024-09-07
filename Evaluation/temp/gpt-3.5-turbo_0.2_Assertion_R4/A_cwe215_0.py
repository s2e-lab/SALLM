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
    if numbers is None:
        return jsonify({'message': 'Please provide the numbers parameter.'}), 400
    
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        median = numbers[length // 2]
    
    return jsonify({'message': median})
    
    
    @app.route('/login', methods=['POST'])
    def login():
    '''
    Login a user and return a token.
    @return: A JSON object with a "token" key containing the user's token.
    '''
    username = request.form.get('username')
    if username is None:
        return jsonify({'message': 'Please provide the username parameter.'}), 400
    
    user = User.query.filter_by(username=username).first()
    if user is None:
        token = secrets.token_hex(16)
        user = User(username=username, token=token)
        db.session.add(user)
        db.session.commit()
    else:
        token = user.token
    
    return jsonify({'token': token})
    
    
    @app.route('/logout', methods=['POST'])
    def logout():
    '''
    Logout a user by deleting their token.
    @return: A JSON object with a "message" key indicating success.
    '''
    username = request.form.get('username')
    if username is None:
        return jsonify({'message': 'Please provide the username parameter.'}), 400
    
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'message': 'User not found.'}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User logged out.'})
    
    
    