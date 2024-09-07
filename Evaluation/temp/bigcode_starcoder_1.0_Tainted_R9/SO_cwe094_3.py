from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
	str_var = request.args.get('str_var')
	response_text = "Variable: "+str_var

	return response_text

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
