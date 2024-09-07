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
    variable = str_var.split('*')

    if len(variable) > 1:
        return str_var
    else:
        return "Неверное значение. Пожалуйста, введите не пустое значение"

@app.route('/del')
def delete():
    '''
    Delete a variable from the request.
    Return the new string.
    '''
    var_del = request.args.get('var_del')
    variable = var_del.split('*')
    if len