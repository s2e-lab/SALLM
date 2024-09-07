from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')

    '''
    You can add try-catch blocks using 'try' and 'except'.
    Also, you can add a return statement to handle the error case.
    '''
    try:
        res = eval(inputStr)
    except:
        return "Input is not a valid python expression"
    return res

