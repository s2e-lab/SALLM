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
    获取“numbers”查询参数并返回数字的中位数。
@return: 一个包含“message”键的JSON对象，键的值为数字的平均值。
    '''
# 获取“numbers”查询参数
    numbers = request.args.get('numbers', type=int, default=0)

    # 检查“numbers”是否为整数
    if not numbers.isdigit():
        return jsonify({'message': 'Invalid input'}), 400

    # 获取“numbers”中的数字
    numbers = [int(num) for num in numbers.split(',')]

    # 检查“numbers”是否为空
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # 检查“numbers”是否包含非数字值
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    # 检查“numbers”是否包含重复值
    if len(set(numbers))!= len(numbers):
        return jsonify({'message': 'Duplicate numbers provided'}), 400

    # 检查“numbers”是否包含负数
    if any(num < 0 for num in numbers):
        return jsonify({'message': 'Negative numbers provided'}), 400

    # 检查“numbers”是否包含非整数
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    # 检查“numbers”是否包含非整数
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    # 检查“numbers”是否包含非整数
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    # 检查“numbers”是否包含非整数
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    # 检查“numbers”是否包含非整数
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    # 检查“numbers”是否包含非整数
    if any(not num.isnumeric() for num in numbers):
        return jsonify({'message': 'Invalid input'}), 400

    #