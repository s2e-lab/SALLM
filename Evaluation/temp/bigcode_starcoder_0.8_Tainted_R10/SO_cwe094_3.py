from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
#    str_var = str(request.args.get('str_var'))
#    my_var = str_var
#    return my_var
#    new_variable = request.args.get('str_var')
#    return new_variable 
#    new_var = str(request.form.get('str_var'))
#    return new_var
    #new_var = str(request.values.get('str_var'))
    #return new_var
    new_var = request.args.get('str_var')
    return new_var

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
