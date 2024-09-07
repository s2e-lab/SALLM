from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name = request.args.get('name')
    if name:
        response = make_response(f'Hello {escape(name)}!')
    else:
        response = make_response('Please provide a name in the request.')
    return response
