from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    # Extract code from request
    code = request.args.get('code')
    
    # Evaluate code
    try:
        result = eval(code)
    except Exception as e:
        result = str(e)
    
    # Return result
    return str(result)
    
    
    