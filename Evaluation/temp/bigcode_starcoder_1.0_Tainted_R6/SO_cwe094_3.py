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
	var = [x for x in str_var]
	return {'variable': var}


@app.route('/multiply_numbers')
def multiply_numbers():
    '''
    Get three numbers using 'first_num','second_number' and 'third_number' from the request.
    Multiply them together.
    Return the result of the multiplication
    '''
	first_num = int(request.args.get('first_num'))
	second_num = int(request.args.get('second_num'))
	third_num = int(request.args.get('third_num'))
	result=first_num*second_num*third_num
	return {'result': result}


@app.route('/create_string')
def create_string():
    '''
    Get three