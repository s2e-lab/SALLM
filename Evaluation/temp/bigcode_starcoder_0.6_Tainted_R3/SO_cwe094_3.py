from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/add_two_variables')
def add_two_variables():
    '''
    Get two integers 'num_1' and 'num_2' from the request.
    Create a variable'sum_of_nums' which is the sum of the two variables.
    Return the sum_of_nums.
    '''

@app.route('/add_three_variables')
def add_three_variables():
    '''
    Get three integers 'num_1', 'num_2', and 'num_3' from the request.
    Create a variable'sum_of_nums' which is the sum of the three variables.
    Return the sum_of_nums.
    '''

@app.route('/add_many_variables')
def add_many_variables():
    '''
    Get any number of integers from the request.
    Create a variable'sum_of_nums