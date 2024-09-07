from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')
    if inputStr is None:
        return 'ERROR! Please provide the inputStr as a query parameter.'
    try:
        result = eval(inputStr)
    except Exception as e:
        return 'ERROR! InputStr {} is not a valid python expression. Exception: {}'.format(inputStr, e)
    return result
