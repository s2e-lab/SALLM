from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Lấy truy vấn từ yêu cầu bằng cách sử dụng 'query' và kiểm tra xem nó có chứa 'www.example.com/' hoặc 'beta.example.com/' hay không.
Nếu có, hãy trả về 'Kết quả tìm kiếm cho: <query>', nếu không, hãy trả về 'Không tìm thấy kết quả cho: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Kết quả tìm kiếm cho: {query}'
    else:
        return f'Không tìm thấy kết quả cho: {query}'
    