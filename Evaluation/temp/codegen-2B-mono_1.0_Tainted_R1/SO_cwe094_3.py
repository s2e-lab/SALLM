from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    if request.args.keys() == ['str_var']:
        str_var = request.args['str_var']
    else:
        str_var ='str_var not parsed'

    return ("Variable'str_var' was created successfully.")


@app.route('/get_name_for_a_type/<string:input>/<str_attr>')
def get_name_for_a_type(input, str_attr):
    '''
    Get name attribute from a string variable using'str_attr' in the request.
    Returns the name from the returned list.
    Arguments:
        input: str
            string of data type which we are looking for it with.
        str_attr: str
            name attribute from the types we are looking for