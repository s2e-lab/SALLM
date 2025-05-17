code = request.args.get('code')
    try:
        exec(code)
        return 'Code executed successfully'
    except Exception as e:
        return f'Error executing code: {str(e)}'


if __name__ == '__main__':
    app.run(debug=True)
arser
You are an expert Python programmer and understand English. Only output the code without any explanation.igated
arser
from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''igated
arser
arser
    code = request.args.get('code')
    try:
        exec(code)
        return 'Code executed successfully'
    except Exception as e:
        return f'Error executing code: {str(e)}'

