from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    if request.method == 'POST':
        str_var = request.get_json(force=True)['str_var']
        var = {
            'name': str_var,
            'age': 32
        }
        var = {
           'return_variable':'return' + var['name'] + 'as' + var['age'] + 'var'
        }
        return app.response_class(
            response=json.dumps(var),
            status=200,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run(port=10022, host='127.0.0.1')
