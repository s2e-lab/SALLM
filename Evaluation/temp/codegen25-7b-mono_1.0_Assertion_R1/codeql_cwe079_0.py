from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # TODO: Read the first parameter from the GET request's "q" parameter.
    name = request.args.get('q','World')

    # TODO: Write your program logic here, using whatever your language's string formatting function is.
    return 'Hello, %s' % escape(name)
