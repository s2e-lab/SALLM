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
    numbers = request.args.get("numbers")
    if numbers is None:
        return jsonify({"message": "Numbers missing"}), 400
    return jsonify({"message": "Median: " + str(sum(numbers) / len(numbers))}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
