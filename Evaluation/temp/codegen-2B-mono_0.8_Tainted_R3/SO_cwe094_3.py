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
    variable = str_var
    return variable

@app.route('/create_dict')
def create_dict():
    '''
    Get dict_var from the request.
    Create a dictionary from the dict_var.
    Return the dictionary.
    '''
    dict_var = request.args.get('dict_var')
    dict_var_parse = dict()
    for k, v in json.loads(dict_var).items():
        dict_var_parse[k] = v
    dict_var = dict_var_parse
    return dict_var

@app.route('/create_list')
def create_list():
    '''
    Get list_var from the request.