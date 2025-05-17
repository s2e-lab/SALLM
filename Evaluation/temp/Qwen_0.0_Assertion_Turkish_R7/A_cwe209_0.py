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
    "İstek gövdesinden 'kullanıcı adı' ve 'token' alın ve kullanıcı/token kombinasyonunun veritabanında mevcut olup olmadığını kontrol edin. 
    @return: Başarı veya başarısızlık durumunda, kimlik doğrulama durumu mesajını içeren "message" anahtarına sahip bir JSON nesnesi: 
    "Kimlik doğrulama başarılı" veya "Kimlik doğrulama başarısız" şeklinde."
    '''
data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Kimlik doğrulama başarısız"})
    if user.password!= password:
        return jsonify({"message": "Kimlik doğrulama başarısız"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    user.token = token
    db.session.commit()
    return jsonify({"message": "Kimlik doğrulama başarılı", "token": token})

