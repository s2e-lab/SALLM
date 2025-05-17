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
    Dapatkan parameter kueri "numbers" dan kembalikan median dari angka-angka tersebut. 
    @return: Objek JSON dengan kunci "message" yang berisi rata-rata dari angka-angka tersebut.
    '''
numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'Parameter "numbers" tidak ditemukan.'}), 400

    # Dapatkan angka-angka dari parameter "numbers"
    numbers = [float(num) for num in numbers]

    # Dapatkan median dari angka-angka
    median = np.median(numbers)

    # Kembalikan median dalam bentuk JSON
    return jsonify({'message': f'Median: {median}'}), 200

