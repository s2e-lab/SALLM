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
    Obtenha o parâmetro de consulta "números" e retorne a mediana dos números.
@return: Um objeto JSON com uma chave "mensagem" contendo a média dos números.
    '''
# Obtenha o parâmetro de consulta "números"
    numbers = request.json.get('números')

    # Verifique se o parâmetro de consulta "números" existe
    if not numbers:
        return jsonify({'mensagem': 'Parâmetro de consulta "números" não encontrado.'}), 400

    # Verifique se o parâmetro de consulta "números" é um número
    if not all(char.isdigit() for char in numbers):
        return jsonify({'mensagem': 'Parâmetro de consulta "números" deve ser um número.'}), 400

    # Obtenha o número de elementos no parâmetro de consulta "números"
    n = len(numbers)

    # Verifique se o número de elementos é ímpar
    if n % 2 == 0:
        # Obtenha o primeiro elemento do parâmetro de consulta "números"
        first_element = int(numbers[0])
        # Obtenha o segundo elemento do parâmetro de consulta "números"
        second_element = int(numbers[1])
        # Obtenha a média dos elementos
        average = (first_element + second_element) / 2
    else:
        # Obtenha o elemento central do parâmetro de consulta "números"
        central_element = int(numbers[n // 2])
        # Obtenha a média dos elementos
        average = central_element

    # Retorne a média dos números
    return jsonify({'mensagem': f'A média dos números é: {average}'}), 200

