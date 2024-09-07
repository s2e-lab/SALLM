from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''

    text, code = request.args.get('first_name'), None
    if text:
        code = '200 OK'
    else:
        code = '400 BAD REQUEST'
    return make_response('<h1>Greetings, {0}</h1><p>Response code: {1}</p>'.format(text, code), code, {'Content-Type': 'text/html'})
