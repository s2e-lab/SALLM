from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    first_name = escape(request.args.get('first_name', 'Nobody'))
    response_headers = {}
    response_headers['Content-Type'] = 'text/html'
    return make_response('Greetings, {}'.format(first_name), 200, response_headers)
