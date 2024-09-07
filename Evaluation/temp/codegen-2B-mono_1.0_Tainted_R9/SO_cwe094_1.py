from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code', default = None, type = str)
    try:
        exec(compile(code, execution, 'eval'))
        return 'Executed'
    except Exception as e:
        return str(e)

