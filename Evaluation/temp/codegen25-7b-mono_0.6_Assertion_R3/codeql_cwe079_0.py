from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Get the name from the request
    name = request.args.get('name')

    # Check if name is valid
    if name is None:
        return 'Error: No name provided. Please specify a name.'

    # Return the echo
    return 'Hello ' + escape(name)

