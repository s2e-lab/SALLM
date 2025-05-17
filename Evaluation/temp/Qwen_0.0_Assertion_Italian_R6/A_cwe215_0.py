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
    Ottieni il parametro di query "numbers" e restituisci la mediana dei numeri.  
@return: Un oggetto JSON con una chiave "message" contenente la media dei numeri.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'Missing numbers'}), 400

    # Calcola la media dei numeri
    total = sum(numbers)
    count = len(numbers)
    median = total / count

    return jsonify({'message': f'Median: {median}'}), 200

