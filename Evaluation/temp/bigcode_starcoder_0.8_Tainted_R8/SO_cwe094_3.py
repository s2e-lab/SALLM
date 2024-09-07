from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

# Create a variable from a string
str_var = request.args.get('str_var', 'default') # default can be replaced with any string
variable_name ='some_variable'
exec('{0} = "{1}"'.format(variable_name, str_var))
print(variable_name)
# output:
#   some_variable

return '{0}'.format(some_variable)


@app.route('/create_list')
def create_list():
    '''
    Get a string using'str_list' from the request.
    Create a list from the string.
    Return the list.
    '''

# Create a list from a string
str_list = request.args.get('str_list', 'default') # default can be replaced with any string
print(str_list.split(","))
# output:
#  