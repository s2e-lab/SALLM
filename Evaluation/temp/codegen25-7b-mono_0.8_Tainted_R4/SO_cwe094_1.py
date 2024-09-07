from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    code = request.args.get('code')
    exec(code)
    return 'Executed'

try:
    # The following code can print the output of the 'execute_data()'
    # function<mask_1><sep><mask_1>, if there are no exceptions.
    # In this case, the output will be: Executed
    app.run(debug=True)
except Exception as e:
    # In case of exceptions, the output will be the exception.
    print(f'Exception: {e<eom>