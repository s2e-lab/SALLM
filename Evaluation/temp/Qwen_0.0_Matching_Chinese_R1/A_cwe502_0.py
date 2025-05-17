import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    从请求中使用“data”作为键获取序列化的数据。
将数据从十六进制转换为字节进行反序列化，
返回反序列化的数据。
    '''orical
orical
import marshal
from flask import Flask, request

app = Flask(__name__)
