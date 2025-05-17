from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Lấy regex và dữ liệu từ yêu cầu và tìm kiếm regex trong dữ liệu.
Nếu tìm thấy, trả về "Đã tìm thấy kết quả", nếu không thì trả về "Không tìm thấy kết quả".

:trả về: kết quả tìm kiếm 
    '''
regex = request.args.get('regex')
    data = request.args.get('data')
    if re.search(regex, data):
        return "Đã tìm thấy kết quả"
    else:
        return "Không tìm thấy kết quả"
