from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    if code is None:
        return 'No code provided'
    try:
        exec(code)
    except Exception as e:
        return 'Error: ' + str(e)
    return 'Executed'
