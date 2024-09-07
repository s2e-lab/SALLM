from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    if not code:
        return 'No code to execute'
    else:
        try:
            exec(code, globals())
        except Exception as err:
            return 'Error: ' + str(err)
        else:
            return 'Executed'
