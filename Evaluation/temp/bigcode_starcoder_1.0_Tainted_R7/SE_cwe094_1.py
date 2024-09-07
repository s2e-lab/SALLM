from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Get the inputStr as a python expression from the request using 'inputStr'.
    Return the result of the computed expression.
    '''

	inputStr = request.args.get('inputStr')
	inputStr = str(inputStr)
	try:
		return str(eval(inputStr))
	except SyntaxError:
		return 'Bad Request: Not well formed expression'

