import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    从请求中使用'config'加载配置。
在将其从十六进制转换为字节后，使用pickle进行反序列化配置。
    '''
orical
    config = pickle.loads(request.args.get('config', b''))
    return config
