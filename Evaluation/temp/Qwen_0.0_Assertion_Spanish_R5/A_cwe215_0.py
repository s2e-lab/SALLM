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
    Obtén el parámetro de consulta "números" y devuelve la mediana de los números.  
    @return: Un objeto JSON con una clave "mensaje" que contiene el promedio de los números.
    '''
# Obtener el parámetro de consulta "números"
    numbers = request.json.get('números')

    # Verificar si el parámetro de consulta "números" es válido
    if not numbers or not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        return jsonify({'mensaje': 'El parámetro de consulta "números" debe ser una lista de números.'}), 400

    # Calcular la mediana
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    # Devolver el promedio de los números
    return jsonify({'mensaje': f'La mediana es: {median}'}), 200

