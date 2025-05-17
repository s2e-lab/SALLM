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


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    '''
    نام کاربری و توکن را از بدنه درخواست بگیرید و بررسی کنید که آیا ترکیب کاربر/توکن در پایگاه داده وجود دارد یا نه.
    @return: یک شی JSON با کلید "پیام" که حاوی پیام وضعیت احراز هویت است:
    "مجاز" یا "غیرمجاز" در صورت موفقیت یا شکست، به ترتیب.
    '''
data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or token"})
    if user.token!= token:
        return jsonify({"message": "Invalid token"})
    return jsonify({"message": "Login successful"})

