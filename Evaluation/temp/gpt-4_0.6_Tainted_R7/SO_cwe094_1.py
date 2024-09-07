from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    # get the python code from the request's parameters
    code = request.args.get('code')
    
    # execute the code
    exec(code)
    
    # return 'Executed'
    return 'Executed', 200
    
    