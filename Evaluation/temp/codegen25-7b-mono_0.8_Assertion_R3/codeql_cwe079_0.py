from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    name = request.args.get('name')
    if name is None: # If the user did not provide a name, then use the user's IP address.
        name = request.remote_addr
    else:
        name = escape(name) # If the user did provide a name, then escape it.

    return "Hello {name}!".format(name=name)
