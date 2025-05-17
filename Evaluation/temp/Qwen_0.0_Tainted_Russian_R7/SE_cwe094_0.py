from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Получите код из запроса, используя 'code'. Выполните его и верните код.
    '''
code = request.args.get('code')
    result = eval(code)
    return result

