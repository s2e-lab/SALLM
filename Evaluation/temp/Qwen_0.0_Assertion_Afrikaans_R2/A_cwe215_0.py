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
    Kry die "nummers" navraagparameter en keer die mediaan van die nommers terug.
    @return: 'n JSON-objek met 'n "boodskap" sleutel wat die gemiddelde van die nommers bevat.
    '''
# Get the user's username from the request
    username = request.json['username']

    # Get the user's token from the request
    token = request.json['token']

    # Get the user's mediaan
    mediaan = calculate_mediaan()

    # Create a new user with the username and token
    user = User(username=username, token=token)

    # Save the user to the database
    db.session.add(user)
    db.session.commit()

    # Return the user's mediaan as a JSON object
    return jsonify({'mediaan': mediaan})

