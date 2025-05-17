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
    Obtenez le paramètre de requête "numbers" et renvoyez la médiane des nombres.
    @return : Un objet JSON avec une clé "message" contenant la moyenne des nombres.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'Missing numbers'}), 400

    # Convertir les nombres en listes de nombres
    numbers_list = [float(num) for num in numbers]

    # Trier la liste de nombres
    sorted_numbers = sorted(numbers_list)

    # Vérifier si la liste de nombres est paire ou impaire
    if len(sorted_numbers) % 2 == 0:
        # Si la liste est paire, la médiane est la moyenne des deux nombres en milieu
        median = (sorted_numbers[len(sorted_numbers) // 2 - 1] + sorted_numbers[len(sorted_numbers) // 2]) / 2
    else:
        # Si la liste est impaire, la médiane est le nombre en milieu
        median = sorted_numbers[len(sorted_numbers) // 2]

    # Retourner la médiane sous forme de JSON
    return jsonify({'message': median}), 200

