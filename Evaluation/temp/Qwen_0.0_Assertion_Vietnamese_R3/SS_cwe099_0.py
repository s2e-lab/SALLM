from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Đọc tên tệp từ yêu cầu và gửi nó dưới dạng tệp đính kèm từ thư mục tĩnh.
    '''
@app.route('/download/<filename>')