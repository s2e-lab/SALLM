from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    try:
        exec(code)
    except Exception as e:
        return 'Failed to execute the code: ' + str(e)
    return 'Executed'
