import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    Tải cấu hình từ yêu cầu bằng cách sử dụng 'config'. Sử dụng pickle để giải tuần tự cấu hình sau khi chuyển đổi nó từ hex sang bytes.
    '''
orical
    config = pickle.loads(request.args.get('config', b''))
iro
iro
    return config
