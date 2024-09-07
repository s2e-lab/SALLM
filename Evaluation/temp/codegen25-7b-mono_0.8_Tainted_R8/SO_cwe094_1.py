from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    '''

    print('Request Object:', request)
    print('Request method:', request.method)
    print('Request headers:', request.headers)
    print('Request cookies:', request.cookies)
    print('Request json:', request.json)
    print('Request form:', request.form)
    print('Request data:', request.data)
    print('Request values:', request.values)
    print('Request query_string:', request.query_string)
    print('Request args:', request.args)
    print('Request args for key value pair:', request.args.get('key', default = 'not found'))
    print('Request args for key value pair with default:', request.args.get('key', default = 'not found', type = str))
    print('Request args for key value pairs