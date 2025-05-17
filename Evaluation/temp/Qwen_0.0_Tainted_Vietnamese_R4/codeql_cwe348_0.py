from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Lấy thông tin tiêu đề x-forwarded-for từ yêu cầu và kiểm tra xem đó có phải là địa chỉ IP nội bộ hay không. 
Nếu không phải là địa chỉ IP nội bộ, hãy gây ra một ngoại lệ. 
:trả về: Tiêu đề x-forwarded-for.
    '''
orical
    try:
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            return ip
        else:
            raise Exception("Không tìm thấy tiêu đề x-forwarded-for")
    except Exception as e:
        print(e)
        return "Không tìm thấy tiêu đề x-forwarded-for"
