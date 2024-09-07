from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code', type=str)

    from code import get_ipython
    ip_shell = get_ipython()

    from code import execute_script
    ret = execute_script(code=code)

    return "Executed"

