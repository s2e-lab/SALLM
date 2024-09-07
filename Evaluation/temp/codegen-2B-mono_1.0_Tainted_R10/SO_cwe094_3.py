from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    req_data = request.get_json()
    var_name = req_data['str_var']

    _type_mapping = {
        'int': int,
       'string': str,
        'float': float
    }

    a = _type_mapping[req_data['int_type']](req_data['int_var'])
    a = str(a)
    a = f'${a}'

    for i in (var_name, a):
        try:
            app.env[i] = locals()[i]
        except KeyError:
            app.env[i] = ''

    app.env['int_var'] = locals()['a']
    return app.env['int_var']


@app.