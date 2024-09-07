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

    # Parse the JSON from the request body
    data = request.get_json()
    
    # Get the access token from the headers
    token = request.headers.get('Access-Token')
    
    # Authenticate the user
    user = User.query.filter_by(token=token).first()
    
    if not user:
        return jsonify({'message': 'Access denied'}), 403
    
    try:
        # Get the numbers and calculate the median
        numbers = sorted(data['numbers'])
        n = len(numbers)
        median = (numbers[n//2] + numbers[(n-1)//2]) / 2
      
    except KeyError:
        return jsonify({'message': '"numbers" key not found in JSON object'}), 400
    except ValueError:
        return jsonify({'message': 'Invalid number found in "numbers" array'}), 400
    
    return jsonify({'message': 'Median is {}'.format(median)})
  
    
    