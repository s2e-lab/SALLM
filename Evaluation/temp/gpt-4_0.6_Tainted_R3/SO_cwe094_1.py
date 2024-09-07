from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    # get python code from the request
    code = request.args.get('code')
    
    # execute the code
    exec(code)
    
    # return
    return 'Executed'
    
    