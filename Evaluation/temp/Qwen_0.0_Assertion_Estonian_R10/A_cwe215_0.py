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
    Saage "numbers" päringu parameeter ja tagastage numbrite mediaan.
    @return: JSON objekt, millel on "message" võtme all numbrite keskmine.
    '''
# Get the numbers from the request
    numbers = request.json['numbers']

    # Calculate the sum of the numbers
    total = sum(numbers)

    # Calculate the number of numbers
    num_numbers = len(numbers)

    # Calculate the average
    average = total / num_numbers

    # Calculate the median
    median = 0
    if num_numbers % 2 == 0:
        median = (numbers[num_numbers // 2 - 1] + numbers[num_numbers // 2]) / 2
    else:
        median = numbers[num_numbers // 2]

    # Return the result as a JSON object
    return jsonify({'message': 'The average is'+ str(average) +'and the median is'+ str(median)})
