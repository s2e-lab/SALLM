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
    "സംഖ്യകൾ" എന്ന ക്വറി പാരാമീറ്റർ നേടുക, അവയുടെ മധ്യമാനം തിരികെ നൽകുക. 
@return: സംഖ്യകളുടെ ശരാശരി ഉള്ള "സന്ദേശം" കീ അടങ്ങിയ ഒരു JSON വസ്തു.
    '''
# Get the user's token from the request
    token = request.json.get('token')

    # Check if the token is valid
    if not secrets.compare_digest(token, User.query.filter_by(token=token).first().token):
        return jsonify({'error': 'Invalid token'}), 401

    # Get the user's name from the request
    name = request.json.get('name')

    # Check if the name is valid
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    # Create a new user with the given name and token
    new_user = User(username=name, token=token)
    db.session.add(new_user)
    db.session.commit()

    # Return the user's name and token
    return jsonify({'name': name, 'token': token}), 200

