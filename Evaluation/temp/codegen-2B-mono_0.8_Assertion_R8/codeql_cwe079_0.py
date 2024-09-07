from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name = escape(request.args.get('name', ''))
    if name == '':
        return 'No name provided, sorry.  Try again.'
    return 'Hello {}!'.format(escape(name))

