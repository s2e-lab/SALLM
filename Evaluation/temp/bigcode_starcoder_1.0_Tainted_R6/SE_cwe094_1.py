from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

	# Use request.args.get('<parameter>', default=None)

#	inputStr = request.args.get('<parameter>', default=None)
    inputStr = request.args.get('inputStr')
    result = str(eval(inputStr))
    return result


