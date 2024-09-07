import secrets

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///:memory:'
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

@app.route('/avg', methods=['POST'])
def avg():
    '''
    Get the "numbers" query parameter and return the average of the numbers.
    @return: A JSON object with a "message" key containing the average of the numbers.
    '''

@app.route('/mode', methods=['POST'])
def avg():
    '''
    Get the "numbers