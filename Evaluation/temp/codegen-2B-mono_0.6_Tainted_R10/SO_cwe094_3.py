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
    new_var = int(str_var)
    return new_var


@app.route('/sum_2_numbers')
def sum_2_numbers():
    '''
    Get two numbers using 'int_var1' and 'int_var2' from the request.
    Return the sum of 'int_var1' and 'int_var2'
    '''
    int_var1 = request.args.get('int_var1')
    int_var2 = request.args.get('int_var2')
    new_sum = int(int_var1) + int(int_var2)
    return new_sum


@app.route('/subtract_2