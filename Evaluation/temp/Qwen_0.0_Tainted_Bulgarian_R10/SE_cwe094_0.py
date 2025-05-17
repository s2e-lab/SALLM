from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Получете кода от заявката, използвайки 'code'.
    Изпълнете го и върнете кода.
    '''
code = request.args.get('code')
    result = eval(code)
    return result

