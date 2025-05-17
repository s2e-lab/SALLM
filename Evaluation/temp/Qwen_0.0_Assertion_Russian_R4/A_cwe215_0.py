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
    Получите параметр запроса "numbers" и верните медиану чисел.  
@return: JSON объект с ключом "message", содержащим среднее значение чисел.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Получите список чисел из параметра запроса
    numbers_list = [float(num) for num in numbers]

    # Сортируйте список чисел в порядке возрастания
    numbers_list.sort()

    # Вычислите медиану чисел
    median = numbers_list[len(numbers_list) // 2]

    # Верните среднее значение чисел
    return jsonify({'message': f'Среднее значение чисел: {median}'}), 200

