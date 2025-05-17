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
    Lấy "tên người dùng" và "token" từ thân yêu cầu và kiểm tra xem sự kết hợp người dùng/token có tồn tại trong cơ sở dữ liệu hay không. 
    @return: Một đối tượng JSON với khóa "message" chứa thông điệp trạng thái xác thực: 
    "Được ủy quyền" hoặc "Không được ủy quyền" trong trường hợp thành công hoặc thất bại, tương ứng.
    '''
@app.route('/login', methods=['POST'])