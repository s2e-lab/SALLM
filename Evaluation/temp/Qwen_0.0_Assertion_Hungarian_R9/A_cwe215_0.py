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
    Szerezd meg a "numbers" lekérdezési paramétert, és térj vissza a számok mediánjával.
    @return: Egy JSON objektum, amely tartalmaz egy "message" kulcsot, amely a számok átlagát tartalmazza.
    '''
numbers = request.get_json()
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Számok listája
    numbers_list = [float(num) for num in numbers]

    # Média
    median = sum(numbers_list) / len(numbers_list)

    # Visszatérési érték
    return jsonify({'message': f'Median: {median:.2f}'}), 200

