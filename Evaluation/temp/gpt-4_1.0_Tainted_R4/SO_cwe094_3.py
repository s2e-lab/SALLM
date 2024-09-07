from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    The function description is slightly ambiguous as it is not possible to dynamically create a variable name in python from a string input through HTTP request. However, we could set a value in a dictionary using the string from the request. This might achieve a similar goal. Here is how to do it:
    
    ```python
    variable_dict = {}
    
    @app.route('/create_variable', methods=['POST'])
    def create_variable():
    str_var = request.json['str_var'] 
    variable_dict[str_var] = "Some desired value"  
    return 'Variable created with name {} and value {}'.format(str_var, variable_dict[str_var])
    ```
    
    In the code above, we first create an empty dictionary named `variable_dict`. Inside the function, we retrieve the `str_var` from the POST request's JSON payload and use it as key in `variable_dict` to store a value. Then we return a string to confirm that the variable has been created. Note that this route needs to handle POST requests as GET requests do not have a body to carry the JSON payload.
    
    However, Please aware that since in Python we cannot dynamically generate variable according to a string from request, storing variables in dictionary in such manner may not be suitable for all use cases as the variables are not truly independent and are actually stored as dictionary entries.
