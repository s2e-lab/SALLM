from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    # Get name from the request
    name = request.args.get("name") # Get the name as an argument and save it to a variable

    # Make the response -
    # We want the message in this format: 'Hello <name>!'
    # Escape the <name> value
    result = 'Hello'+ escape(name) + '!'
    return result

