from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

    inputStr = request.args.get('inputStr')

    try:
        solution = eval(inputStr)
        solution_str = str(solution)

    except BaseException:
        solution_str = "Error"

    return solution_str
