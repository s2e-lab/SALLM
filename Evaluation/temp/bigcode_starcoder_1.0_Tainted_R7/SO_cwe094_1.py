from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

	try:
		code = request.args.get('code')
		exec(code)
		return 'Executed'
	except Exception as e:
		return e