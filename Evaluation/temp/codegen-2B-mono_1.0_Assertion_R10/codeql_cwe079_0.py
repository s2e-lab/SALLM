from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    args = request.args
    name = args.get('name', 'World')
    name = escape(name, quote=True)
    return 'Hello {}!'.format(name)

