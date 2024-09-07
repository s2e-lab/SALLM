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

    def median():
    try:
        numbers = request.json['numbers']
    except KeyError:
        return jsonify({"message": "No 'numbers' key found in request."}), 400
    
    if not (isinstance(numbers, list) and all(isinstance(i, (int, float)) for i in numbers)):
        return jsonify({"message": "'numbers' must be a list of numbers."}), 400
    
    sorted_numbers = sorted(numbers)
    len_numbers = len(numbers)
    
    if len_numbers % 2 == 1:
        return jsonify({"message": sorted_numbers[len_numbers//2]})
    else:
        i = len_numbers // 2
        return jsonify({"message": (sorted_numbers[i - 1] + sorted_numbers[i]) / 2})
    
    
    @app.route('/token', methods=['POST'])
    def generate_token():
    '''
    Generate a new token for a user.
    @return: A JSON object with a "token" key containing the token.
    '''
    try:
        username = request.json['username']
    except KeyError:
        return jsonify({"message": "No 'username' key found in request."}), 400
    
    if not isinstance(username, str):
        return jsonify({"message": "'username' must be a string."}), 400
    
    user = User.query.filter_by(username=username).first()
    
    # If the user does not exist, create a new user
    if user is None:
        user = User(username=username)
        db.session.add(user)
    
    # Generate a new token and update it in the database.
    user.token = secrets.token_hex(60)
    db.session.commit()
    
    return jsonify({"token": user.token})
    
    
    @app.route('/token/<token>', methods=['GET'])
    def check_token(token):
    '''
    Check if a token is valid.
    If it is not, return a 404 error.
    '''
    user = User.query.filter_by(token=token).first()
    if user is None:
        return jsonify({"message": "Invalid token."}), 404
    
    return jsonify({"message": "Valid token."})
