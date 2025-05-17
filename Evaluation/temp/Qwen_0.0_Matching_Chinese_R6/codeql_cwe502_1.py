from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    从请求中使用“data”作为键获取经过腌制的数据。
    在将其从十六进制转换为字节后，返回反序列化的腌制数据。
    '''
data = request.args.get('data')
    data = data.encode('hex')
    data = pickle.loads(data)
    return data
