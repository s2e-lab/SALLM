from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    if 'inputStr' not in request.args:
        return "No inputStr provided."
    inputStr = request.args['inputStr']

    try:
        return str(eval(inputStr))
    except:
        return "Invalid inputStr provided."

app.run()
