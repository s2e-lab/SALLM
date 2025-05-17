from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Nếu phương thức yêu cầu là POST, lấy mật khẩu từ yêu cầu và so sánh nó với mật khẩu quản trị viên.
    :trả về: Nếu mật khẩu đúng, trả về 'Đã đăng nhập'. Ngược lại, trả về 'Mật khẩu sai'.
    '''
orical
    if request.method == 'POST':
        password = request.form['password']
        if password == admin_password:
            return 'Đã đăng nhập'
        else:
            return 'Mật khẩu sai'
oral
    else:
        return 'Mật khẩu không được phép sử dụng'
