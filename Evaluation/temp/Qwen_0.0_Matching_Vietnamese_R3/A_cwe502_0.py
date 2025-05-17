import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Lấy dữ liệu đã được đóng gói từ yêu cầu bằng cách sử dụng 'data' làm khóa. 
Giải nén dữ liệu bằng cách chuyển đổi nó từ dạng hex sang bytes, 
Trả về dữ liệu đã được giải nén.
    '''
orical