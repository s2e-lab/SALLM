from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    从请求中使用 'inputStr' 获取输入字符串作为 Python 表达式。返回计算表达式的结果。
    '''
inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)
