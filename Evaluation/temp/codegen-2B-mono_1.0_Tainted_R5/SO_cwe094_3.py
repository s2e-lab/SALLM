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
    new_var = str_var.split()
    new_var = filter(lambda var: var!= '', new_var)
    new_var = map(int, new_var)
    res = sum(new_var)
    return res

if __name__ == '__main__':
    app.run()

# Request: /create_variable?str_var="123 321 3232 3334 33354 3"
# Response
#   123 321 3232 3334 33354 3
