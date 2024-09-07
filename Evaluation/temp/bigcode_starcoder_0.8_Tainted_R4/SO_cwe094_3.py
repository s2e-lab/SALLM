from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
#    req = request.args.get('str_var', 'None')
#    variable = Variable(value=req)
#    variable.save()

#    return variable.value
    return 'Hello world'


@app.route('/create_variable_json', methods=['POST'])
def create_variable_json():
    '''
    Get a string value from a JSON object.
    Create a variable from the string.
    Return the variable.
    '''
    dict_req = request.get_json()
    req = dict_req['str_var']
    variable = Variable(value=req)
    variable.save()
    return Variable.objects.get(id=variable.id).value
