from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    str_var = str(request.args.get('var'))
    
    # Try creating a new variable from the string;
    # return HTTP error 400 if the string can't be cast into a variable
    try:
        myvar = str_var
    except Exception as e:
        print('Error: ' + str(e))
        return '', 400
    
    # Return the variable
    return myvar



