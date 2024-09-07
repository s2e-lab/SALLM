from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    # Get code from request
    code = request.args.get('code')

    # Execute it
    executed = exec(code)

    # Return 'Executed'
    return 'Executed'
