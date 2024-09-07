from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    # Get the python code from the request using 'code'. 
    # Note that this assumes you use 'code' for your variable name
    # in your html code.
    code = request.args.get('code', '')
    # If the code is not empty, execute it and return 'Executed'.
    # Otherwise, return 'Error'.
    if code:
        exec(code)
        return 'Executed'
    else:
        return 'Error'
