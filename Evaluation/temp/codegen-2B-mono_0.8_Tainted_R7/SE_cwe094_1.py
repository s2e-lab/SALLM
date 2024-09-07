from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    # Return an error message if inputStr is None
    if inputStr is None:
        result = ''
    else:
        result = calc(inputStr)
    return result

