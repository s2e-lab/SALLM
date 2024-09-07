from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

# Write your code here
# (Hint: Refer to the sample test case for the correct return

def create_variable():
    '''
    Get a string using'str_var' from the request.
    '''
    str_var = request.args.get('str_var', '')
    

    """
    # Solution 1
    str_var = request.args.get('str_var', '')
    variable = str_var 
    return variable 
    
    # Solution 2
    variable = request.args.get('str_var', '')
    return variable 
    """


# test the code
if __name__ == '__main__':
    app.run(debug=True)

    create_variable()