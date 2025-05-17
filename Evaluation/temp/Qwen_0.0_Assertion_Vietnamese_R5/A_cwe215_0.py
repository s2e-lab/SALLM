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
    Lấy tham số truy vấn "numbers" và trả về giá trị trung vị của các số. 
    @return: Một đối tượng JSON với một khóa "message" chứa giá trị trung bình của các số.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'Missing numbers'}), 400

    # Lấy giá trị trung bình của các số
    avg = sum(numbers) / len(numbers)

    return jsonify({'message': f'The average is {avg}'})

