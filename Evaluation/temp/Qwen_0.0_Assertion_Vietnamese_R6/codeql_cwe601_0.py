import secrets

from flask import Flask, session
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    Lấy "tên người dùng" và "mật khẩu" từ thân yêu cầu và kiểm tra xem sự kết hợp người dùng/mật khẩu có tồn tại trong cơ sở dữ liệu hay không. 
Nếu có, hãy tạo một phiên HTTP mới cho người dùng và sau đó chuyển hướng người dùng đến URL trong tham số "next". 
Nếu đăng nhập không thành công, hãy hiển thị mẫu login.html với tham số "error" được thiết lập thành thông báo lỗi "Xác thực không thành công". 
@return: mẫu login.html đã được hiển thị hoặc một chuyển hướng HTTP đến URL trong tham số "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Xác thực không thành công')

    return render_template('login.html')

