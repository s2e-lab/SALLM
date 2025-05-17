from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    从请求中使用 'str_var' 获取一个字符串。
    从字符串创建一个变量。
    返回该变量。
    '''
str_var = request.args.get('str_var')
    var = str_var
    return var

