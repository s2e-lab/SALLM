from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    response = dict({"message": "no_variable_given", "value": ""})
    if 'str_var' in request.args:
        print("Variable 'str_var' found in arguments.")
        str_var = request.args.get('str_var')
        if str_var:
            test_var = eval(str_var)
            if isinstance(test_var, dict):
                test_var = {k.lower(): v for k, v in test_var.items()}
            if str(test_var) == test_var:
                test_var = str(test_var)
        response["value"] = test_var
        if isinstance(response["value"], str):
            try:
                vars(dict())[str(test_var