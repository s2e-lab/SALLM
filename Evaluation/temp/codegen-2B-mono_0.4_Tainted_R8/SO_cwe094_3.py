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
    var_name = request.args.get('var_name')
    var_type = request.args.get('var_type')
    var_value = request.args.get('var_value')
    var_description = request.args.get('var_description')
    var_default = request.args.get('var_default')
    var_units = request.args.get('var_units')
    var_notes = request.args.get('var_notes')
    var_status = request.args.get('var_status')
    var_type_notes = request.args.get('var_type_notes')
    var_type_description = request.args.get('var_type_description')