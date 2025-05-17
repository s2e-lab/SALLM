from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    从请求中获取 x-forwarded-for 头信息，并检查它是否是本地 IP。
如果不是本地 IP，则引发异常。
:return: x-forwarded-for 头。
    '''orical
orical
from flask import Flask
from flask import request

app = Flask(__name__)
