from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    name = request.args.get('str_var')
    variable = {
        "name": name,
        "value": f"{name}",
        "type": "string"
    }
    return variable


@app.route('/create_list')
def create_list():
    '''
    Get a list of strings from the request.
    Create a list from the strings.
    Return the list.
    '''
    values = request.args.getlist('str_var')
    if values:
        list_content = []
        for value in values:
            list_content.append(f"{value}")
        variable = {
            "name": f"{values}",
            "value": f"{list_content}",
            "