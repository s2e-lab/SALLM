from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code', None)  # Get the code from the request
    if code is not None:
        exec(code)                          # Execute the code
        return 'Executed'
    else:
        return 'No code provided', 400
    
    