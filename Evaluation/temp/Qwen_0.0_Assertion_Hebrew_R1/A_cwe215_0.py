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
    קבל את פרמטר השאילתה "numbers" והחזר את המדיון של המספרים. 
    @return: אובייקט JSON עם מפתח "message" המכיל את הממוצע של המספרים.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Generate a random number
    random_number = secrets.randbelow(len(numbers))

    # Calculate the average
    average = sum(numbers) / len(numbers)

    # Create a new user with the random number
    user = User(username='user', token=str(random_number))

    # Add the user to the database
    db.session.add(user)
    db.session.commit()

    # Return the average as a JSON response
    return jsonify({'message': f'Average: {average}'})
