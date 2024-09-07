from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    try:
        inputStr = request.args.get('inputStr', default = None, type = str)
        if inputStr is not None:
            result = eval(inputStr)
            return str(result)
        else:
            return "Invalid input or no input provided"
    except Exception as e:
        return 'Error processing request. Exception: {}'.format(e)
    
    