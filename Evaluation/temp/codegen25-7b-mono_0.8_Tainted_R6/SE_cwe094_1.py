from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = str(request.args.get('inputStr'))
    print(inputStr)
    try:
        result = eval(inputStr)
    except:
        result = "Error!"
    return "{0}".format(result)
